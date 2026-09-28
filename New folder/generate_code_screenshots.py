import os
import subprocess
import html
import pygments
from pygments.lexers import HtmlLexer
from pygments.formatters import HtmlFormatter

EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
if not os.path.exists(EDGE_PATH):
    EDGE_PATH = r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"
if not os.path.exists(EDGE_PATH):
    EDGE_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

CSS_VSCODE = """
* { box-sizing: border-box; }
body {
    margin: 0;
    padding: 10px;
    background: #181818;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
}
.vscode-window {
    width: 980px;
    background: #1e1e1e;
    border-radius: 6px;
    overflow: hidden;
    border: 1px solid #333333;
}
.titlebar {
    background: #323233;
    height: 30px;
    display: flex;
    align-items: center;
    padding: 0 12px;
    font-size: 12px;
    color: #cccccc;
    justify-content: space-between;
}
.window-controls { display: flex; gap: 7px; }
.circle { width: 11px; height: 11px; border-radius: 50%; }
.close { background: #ff5f56; }
.min { background: #ffbd2e; }
.max { background: #27c840; }
.tabbar {
    background: #252526;
    height: 34px;
    display: flex;
    align-items: flex-end;
    border-bottom: 1px solid #1e1e1e;
}
.tab {
    background: #1e1e1e;
    color: #ffffff;
    font-size: 12px;
    padding: 8px 16px;
    border-top: 2px solid #0078d4;
    display: flex;
    align-items: center;
    gap: 8px;
}
.tab-icon { color: #e34c26; font-weight: bold; }
.breadcrumbs {
    background: #1e1e1e;
    padding: 5px 16px;
    font-size: 11.5px;
    color: #888888;
    border-bottom: 1px solid #282828;
    font-family: 'Segoe UI', sans-serif;
}
.editor {
    display: flex;
    padding: 8px 0;
    background: #1e1e1e;
    font-family: Consolas, 'Courier New', monospace;
    font-size: 13px;
    line-height: 19px;
}
.line-numbers {
    width: 55px;
    text-align: right;
    padding-right: 18px;
    color: #858585;
    user-select: none;
    border-right: 1px solid #252526;
}
.code-content {
    flex: 1;
    color: #d4d4d4;
    padding-left: 16px;
    white-space: pre;
    overflow-x: hidden;
}
.statusbar {
    background: #007acc;
    color: #ffffff;
    font-size: 11px;
    height: 22px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 12px;
    font-family: 'Segoe UI', sans-serif;
}

/* VS Code Dark+ Syntax Highlighting */
.cp { color: #569cd6; } /* doctype */
.p { color: #808080; } /* tag angle brackets < > */
.nt { color: #569cd6; font-weight: normal; } /* tag name */
.na { color: #9cdcfe; } /* attribute name */
.s, .s1, .s2 { color: #ce9178; } /* attribute value / string */
.o { color: #d4d4d4; } /* operator = */
.c, .cm, .c1 { color: #6a9955; font-style: italic; } /* comments */
.m, .mi, .mf { color: #b5cea8; } /* numbers */
.k, .kd { color: #569cd6; }
.nf { color: #dcdcaa; }
.nc { color: #4ec9b0; }
"""

def render_code_screenshot(file_path, start_line, end_line, output_png_path, part_label=""):
    with open(file_path, "r", encoding="utf-8") as f:
        all_lines = f.readlines()
    
    total_lines = len(all_lines)
    s_idx = max(0, start_line - 1)
    e_idx = min(total_lines, end_line)
    
    selected_lines = all_lines[s_idx:e_idx]
    actual_count = len(selected_lines)
    
    code_text = "".join(selected_lines)
    highlighted_code = pygments.highlight(code_text, HtmlLexer(), HtmlFormatter(nowrap=True))
    
    line_nums = "<br>".join(str(i) for i in range(start_line, start_line + actual_count))
    
    fname = os.path.basename(file_path)
    tag_breadcrumb = "html > body"
    if "tugas" in fname:
        tag_breadcrumb = "cysa html > tugas.html > html > body > table"
    elif "semantic" in fname:
        tag_breadcrumb = "cysa html > semantic.html > html > body > main"
    elif "form" in fname:
        tag_breadcrumb = "cysa html > form.html > html > body > form > fieldset"

    html_page = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>{CSS_VSCODE}</style>
</head>
<body>
<div class="vscode-window">
    <div class="titlebar">
        <div class="window-controls">
            <div class="circle close"></div>
            <div class="circle min"></div>
            <div class="circle max"></div>
        </div>
        <div>{fname} - Visual Studio Code {part_label}</div>
        <div style="width: 40px;"></div>
    </div>
    <div class="tabbar">
        <div class="tab">
            <span class="tab-icon">&lt;&gt;</span>
            <span>{fname}</span>
        </div>
    </div>
    <div class="breadcrumbs">{tag_breadcrumb}</div>
    <div class="editor">
        <div class="line-numbers">{line_nums}</div>
        <div class="code-content">{highlighted_code}</div>
    </div>
    <div class="statusbar">
        <div>Ln {start_line}, Col 1 &nbsp;&nbsp;&nbsp; Spaces: 2 &nbsp;&nbsp;&nbsp; UTF-8 &nbsp;&nbsp;&nbsp; HTML</div>
        <div>Port: 5500 &nbsp;&nbsp;&nbsp; Live Server &nbsp;&nbsp;&nbsp; Go Live</div>
    </div>
</div>
</body>
</html>"""

    temp_html = "temp_vscode_render.html"
    with open(temp_html, "w", encoding="utf-8") as f:
        f.write(html_page)

    # Calculate window height dynamically so entire snippet is fully captured
    # Header (~95px) + code lines * 19px + statusbar (22px) + padding (30px)
    est_height = 110 + (actual_count * 19) + 40
    window_h = max(350, est_height + 30)

    cmd = [
        EDGE_PATH,
        "--headless=new",
        "--disable-gpu",
        f"--screenshot={os.path.abspath(output_png_path)}",
        f"--window-size=1020,{window_h}",
        f"file:///{os.path.abspath(temp_html)}"
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    if os.path.exists(temp_html):
        os.remove(temp_html)
        
    print(f"Generated: {output_png_path} (Lines {start_line} - {start_line + actual_count - 1}, {actual_count} lines, size: {os.path.getsize(output_png_path)} bytes)")

def generate_all():
    os.makedirs("assets/screenshots", exist_ok=True)

    print("=== Generating Code Screenshots for tugas.html (189 lines) ===")
    # 3 parts covering all 189 lines
    render_code_screenshot("tugas.html", 1, 65, "assets/screenshots/code_tugas_part1.png", "(Bagian 1: Baris 1 - 65)")
    render_code_screenshot("tugas.html", 66, 125, "assets/screenshots/code_tugas_part2.png", "(Bagian 2: Baris 66 - 125)")
    render_code_screenshot("tugas.html", 126, 189, "assets/screenshots/code_tugas_part3.png", "(Bagian 3: Baris 126 - 189)")
    # Also overwrite code_tugas_html.png with part 1 so legacy references work
    render_code_screenshot("tugas.html", 1, 65, "assets/screenshots/code_tugas_html.png", "(Baris 1 - 65)")

    print("\n=== Generating Code Screenshots for semantic.html (198 lines) ===")
    # 3 parts covering all 198 lines
    render_code_screenshot("semantic.html", 1, 70, "assets/screenshots/code_semantic_part1.png", "(Bagian 1: Baris 1 - 70)")
    render_code_screenshot("semantic.html", 71, 137, "assets/screenshots/code_semantic_part2.png", "(Bagian 2: Baris 71 - 137)")
    render_code_screenshot("semantic.html", 138, 198, "assets/screenshots/code_semantic_part3.png", "(Bagian 3: Baris 138 - 198)")
    render_code_screenshot("semantic.html", 1, 70, "assets/screenshots/code_semantic_html.png", "(Baris 1 - 70)")

    print("\n=== Generating Code Screenshots for form.html (227 lines) ===")
    # 3 parts covering all 227 lines
    render_code_screenshot("form.html", 1, 75, "assets/screenshots/code_form_part1.png", "(Bagian 1: Baris 1 - 75)")
    render_code_screenshot("form.html", 76, 155, "assets/screenshots/code_form_part2.png", "(Bagian 2: Baris 76 - 155)")
    render_code_screenshot("form.html", 156, 227, "assets/screenshots/code_form_part3.png", "(Bagian 3: Baris 156 - 227)")
    render_code_screenshot("form.html", 1, 75, "assets/screenshots/code_form_html.png", "(Baris 1 - 75)")

    print("\nALL CODE SCREENSHOTS SUCCESSFULLY GENERATED FROM TOP TO BOTTOM!")

if __name__ == '__main__':
    generate_all()
