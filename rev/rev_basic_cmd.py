import sys
from tkinter import filedialog

def main():
    if len(sys.argv) < 2:
        print("Usage: python <script path> <absolute path>")
        print("Example: python F:\\ffl.py F:\\test.txt")
        return

    filename = sys.argv[1]
    global text_input

    try:
        with open(filename, 'r') as file:
            text_input = file.read()
            #print(text_input)
    except FileNotFoundError:
        print("File Not Found: Use the absolute path.")
        exit()
    except PermissionError:
        print("Permission Required: Run CMD as Administrator.")
    except:
        print("HAHAHA Error! Wag ka na mag review.")

    html_body_color = '#2e2e2e'
    html_font_color_code = '#493b2b'
    html_bg_color_code = '#a79987'
    card_padding_px = 5

    text_output = f"""<html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Warning!</title><link rel = "icon" href = "https://assets.stickpng.com/images/5a81af7d9123fa7bcc9b0793.png" type = "image/x-icon"><style>
    .censored {{ background-color: {html_font_color_code}; color: {html_font_color_code}; cursor: pointer;}} .revealed {{ background-color: {html_bg_color_code}; color: {html_font_color_code}; cursor: pointer;}} p{{color: {html_font_color_code}; background-color: {html_bg_color_code};}} body {{background-color: {html_body_color}; }} .cyan-border {{ padding: {card_padding_px}px; font-family: 'Roboto', 'Helvetica', Arial, sans-serif; border-radius: 0px; background-color: {html_bg_color_code}; color: {html_font_color_code}; padding-bottom: 1rem; margin-bottom: 5px; line-height: 1.5;}} h1{{justify-content: center; align-items: center;color: {html_font_color_code};}} h3{{line-height: 1;}}
    </style></head><body><div class="cyan-border">"""

    isTitle = False
    counter = 0
    for i in range((len(text_input)-1)):
        if text_input[i] == '`' and counter > 0: text_output += """</div><br><div class="cyan-border">"""
        elif text_input[i] == '`' and counter == 0: text_output += ''
        elif text_input[i] == '#' and (text_input[i-1] == '\n' or text_input[i-1] == '`'):
            text_output += '<b>'
            isTitle = True
        elif text_input[i] == '#':
            if isTitle == True:
                text_output += '</b>'
                isTitle = False
            else:
                text_output += '<b>'
                isTitle = True
        elif text_input[i] == '\n':
            if isTitle == True:
                text_output += '</b>'
                isTitle = False
            if text_input[i+1] == '`' or text_input[i+1] == '\n': continue
            else: text_output += "<br>"
        elif text_input[i] == '[':
            text_output += f"""<b><span class="censored" onclick="toggleVisibility(this)" style="color: {html_font_color_code};">"""
        elif text_input[i] == '\t':
            text_output += '&emsp;'
        elif text_input[i] == ']':
            text_output += """</span></b>"""
        else:
            text_output += text_input[i]
        counter+=1 
    
    text_output += """</div>
    <script>
    const cyanBorderDivs = document.querySelectorAll('.cyan-border');
    const cyanBorderArray = Array.from(cyanBorderDivs);
    for (let i = cyanBorderArray.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [cyanBorderArray[i], cyanBorderArray[j]] = [cyanBorderArray[j], cyanBorderArray[i]];
    }
    const container = document.body;
    container.innerHTML = '';
    cyanBorderArray.forEach((div) => {
        container.appendChild(div);
    });
    function toggleVisibility(element) {
        if (element.classList.contains("censored")) {
                element.classList.remove("censored");
                element.classList.add("revealed");
        } else {
            element.classList.remove("revealed");
            element.classList.add("censored");
        }
    }
    </script></body></html>"""

    file_path = filedialog.asksaveasfilename(defaultextension=".html",
                                             filetypes=[("HTML Files", "*.html")])

    if file_path:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(text_output)
            print(f'OPEN IN BROWSER: {file_path}')

if __name__ == "__main__":
    main()
