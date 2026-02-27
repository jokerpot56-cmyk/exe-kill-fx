import os
import tkinter as tk
from tkinter import filedialog, messagebox

# الكود الكامل للملف timecycle_mods_4.xml
TIME_CYCLE_XML = """<?xml version="1.0" encoding="UTF-8"?>
<timecycle_modifier_data version="1.000000">
    <modifier name="default" numMods="0" userFlags="0"/>
    <!-- ضع هنا باقي محتوى الملف اللي بعتهولك بالكامل -->
</timecycle_modifier_data>
"""

# قائمة ألوان جاهزة للمود (Kill FX)
COLORS = {
    "Red": {"light_dir_col_r": 1.0, "light_dir_col_g": 0.0, "light_dir_col_b": 0.0},
    "Green": {"light_dir_col_r": 0.0, "light_dir_col_g": 1.0, "light_dir_col_b": 0.0},
    "Blue": {"light_dir_col_r": 0.0, "light_dir_col_g": 0.0, "light_dir_col_b": 1.0},
    # ممكن تضيف ألوان تانية حسب رغبتك
}


def apply_color_mod(xml_content, color_dict):
    """
    تعديل اللون في XML string حسب اختيار المستخدم.
    هنا مثال لتعديل light_dir_col_r/g/b في hud_def_desat_cold_kill
    """
    for channel in ["r", "g", "b"]:
        old = f"<light_dir_col_{channel}>0.255 1.000</light_dir_col_{channel}>"
        new_val = color_dict[f"light_dir_col_{channel}"]
        xml_content = xml_content.replace(
            old,
            f"<light_dir_col_{channel}>{new_val:.3f} 1.000</light_dir_col_{channel}>",
        )
    return xml_content


def create_xml_file(fivem_path, color_choice):
    data_path = os.path.join(fivem_path, "citizen", "common", "data", "timecycle")
    os.makedirs(data_path, exist_ok=True)
    file_path = os.path.join(data_path, "timecycle_mods_4.xml")

    xml_content = apply_color_mod(TIME_CYCLE_XML, COLORS[color_choice])

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(xml_content)

    messagebox.showinfo(
        "تم",
        (
            f"تم إنشاء الملف وتطبيق اللون '{color_choice}' بنجاح!\n"
            f"المسار:\n{file_path}"
        ),
    )


# واجهة البرنامج باستخدام Tkinter
def main():
    root = tk.Tk()
    root.title("Kill FX Tool")
    root.geometry("400x200")
    root.resizable(False, False)

    def choose_folder():
        folder = filedialog.askdirectory(title="اختر مسار FiveM.app")
        if folder:
            path_var.set(folder)

    def apply_changes():
        fivem_path = path_var.get().strip()
        color_choice = color_var.get()

        if not fivem_path or not os.path.exists(fivem_path):
            messagebox.showerror("خطأ", "يرجى اختيار مسار صالح لـ FiveM.app")
            return

        if color_choice not in COLORS:
            messagebox.showerror("خطأ", "يرجى اختيار لون صالح")
            return

        create_xml_file(fivem_path, color_choice)

    path_var = tk.StringVar()
    color_var = tk.StringVar(value="Red")

    tk.Label(root, text="اختر مسار FiveM.app:").pack(pady=5)
    tk.Entry(root, textvariable=path_var, width=50).pack(padx=10)
    tk.Button(root, text="اختر المجلد", command=choose_folder).pack(pady=5)

    tk.Label(root, text="اختر لون Kill FX:").pack(pady=5)
    tk.OptionMenu(root, color_var, *COLORS.keys()).pack()

    tk.Button(root, text="تطبيق", command=apply_changes, bg="#4CAF50", fg="white").pack(
        pady=15
    )

    root.mainloop()


if __name__ == "__main__":
    main()
