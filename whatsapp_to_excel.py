import os
import pandas as pd  # type: ignore
import re
from datetime import datetime

message_pattern = re.compile(r"^(\d{1,2}/\d{1,2}/\d{4}), (\d{1,2}:\d{2}\s?[ap]\.?\s?m\.?) - (.+): (.+)$")
system_message_pattern = re.compile(r"(\d{1,2}/\d{1,2}/\d{4}), (\d{1,2}:\d{2}\s?[ap]\.?\s?m\.?) - .*cifrado de extremo a extremo.*")

def clean_text(text):
    text = text.replace('\u202F', ' ').replace('\xa0', ' ').strip()
    return text

def parse_chat_file(file_path, start_date, end_date):
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    chat_data = []
    current_date, current_time, current_user, current_message = None, None, None, ""

    print(f"\U0001F4C2 Procesando archivo: {file_path}")

    for line in lines:
        line = clean_text(line)
        if system_message_pattern.match(line):
            continue

        match = message_pattern.match(line)

        if match:
            if current_date and start_date <= current_date <= end_date:
                chat_data.append([f"{current_date.strftime('%d/%m/%Y')} {current_time}", current_user, current_message])
            
            date_str, time_str, user, message = match.groups()
            try:
                current_date = datetime.strptime(date_str, "%d/%m/%Y")
            except ValueError:
                continue
            
            if start_date <= current_date <= end_date:
                current_time, current_user, current_message = time_str, user, message
        
        elif current_date and start_date <= current_date <= end_date:
            current_message += " " + line.strip()

    if current_date and start_date <= current_date <= end_date:
        chat_data.append([f"{current_date.strftime('%d/%m/%Y')} {current_time}", current_user, current_message])
    
    if chat_data:
        chat_data.append(["", "", ""])  # Agregar fila en blanco al final del archivo procesado
    
    return chat_data

def save_to_excel(chat_files, start_date, end_date, output_file):
    all_data = []
    for chat_file in chat_files:
        chat_data = parse_chat_file(chat_file, start_date, end_date)
        all_data.extend(chat_data)

    if not all_data:
        print("⚠ No se encontraron mensajes dentro del rango de fechas.")
        return

    df = pd.DataFrame(all_data, columns=["Fecha y Hora", "Remitente", "Mensaje"])

    try:
        df.to_excel(output_file, index=False, engine='openpyxl')
        print(f"✅ Datos guardados en {output_file}")
    except Exception as e:
        print(f"❌ Error al guardar el archivo Excel: {e}")

def main():
    input_dir = input("📂 Ingrese la ruta del directorio con los archivos de chat: ").strip()

    if not os.path.isdir(input_dir):
        print("❌ La ruta proporcionada no es válida.")
        return

    chat_files = [os.path.join(input_dir, file) for file in os.listdir(input_dir) if file.endswith(".txt")]

    if not chat_files:
        print("❌ No se encontraron archivos .txt en el directorio especificado.")
        return

    try:
        start_date_str = input("📅 Ingrese la fecha de inicio (dd/mm/yyyy): ").strip()
        end_date_str = input("📅 Ingrese la fecha de fin (dd/mm/yyyy): ").strip()
        start_date = datetime.strptime(start_date_str, "%d/%m/%Y")
        end_date = datetime.strptime(end_date_str, "%d/%m/%Y")
        if start_date > end_date:
            print("❌ La fecha de inicio no puede ser mayor que la fecha de fin.")
            return
    except ValueError:
        print("❌ Formato de fecha inválido. Use dd/mm/yyyy.")
        return

    current_time = datetime.now().strftime("%Y-%m-%d")
    output_file = f"WhatsApp_Chat_Export_{current_time}.xlsx"
    save_to_excel(chat_files, start_date, end_date, output_file)

if __name__ == "__main__":
    main()
