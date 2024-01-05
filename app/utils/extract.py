
def extract_data(content: bytes):
    phrases = content.decode().split("==========")  # Divide el texto en frases
    
    # Elimina espacios en blanco y líneas vacías
    parts = [phrase.strip() for phrase in phrases if phrase.strip()]
    
    result = []
    for part in parts:
        lines = part.split("\r\n")  # Divide cada parte por líneas
        
        # Si hay al menos dos líneas (nombre del libro y detalles de subrayado)
        if len(lines) >= 2:
            book_name = lines[0].strip()
            details = "\r\n".join(lines[1:-1]).strip()
            phrase = lines[-1].strip()
            
            result.append({
                "book": book_name,
                "phrase": phrase,
                "details": details
            })
    return result
    
