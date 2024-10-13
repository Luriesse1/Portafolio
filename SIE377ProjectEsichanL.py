import tkinter as tk
from tkinter import filedialog
import pandas as pd
import xlsxwriter

SelectedFile = None
OverviewList = [[None for _ in range(2)] for _ in range(8)]

def select_file():
    global SelectedFile

    SelectedFile = filedialog.askopenfilename(
        title="Please select the IMF Inflation Data file:",
        filetypes=[("Excel Files", "*.xlsx")]
    )
    if SelectedFile:
        window.destroy()

window = tk.Tk()
window.title("Tk")

select_button = tk.Button(window, text="Select the file", command=select_file)
select_button.pack(padx=60, pady=60)

window.mainloop()

Data1 = pd.ExcelFile(SelectedFile)

df = pd.read_excel(SelectedFile, sheet_name="Data")
data_df = df.iloc[2:47, 1:7]
df1 = pd.read_excel(SelectedFile, sheet_name="Overview")

with pd.ExcelWriter("Processed_imf_inflation_data.xlsx", engine="xlsxwriter") as writer:
    workbook = writer.book

    worksheet_overview = workbook.add_worksheet("Overview")
    bold1 = workbook.add_format({"bold": True})
    
    OverviewList[0][0] = df1.iloc[6,1]
    OverviewList[1][0] = df1.iloc[7,1]
    OverviewList[2][0] = df1.iloc[8,1]

    OverviewList[3][0] = df1.iloc[9,1]
    OverviewList[4][0] = df1.iloc[18,1]
    OverviewList[5][0] = df1.iloc[19,1]

    OverviewList[6][0] = df1.iloc[20,1]
    OverviewList[7][0] = df1.iloc[4,4]

    OverviewList[0][1] = df1.iloc[6,2]
    OverviewList[1][1] = df1.iloc[7,2]
    OverviewList[2][1] = df1.iloc[8,2]

    OverviewList[3][1] = df1.iloc[9,2]
    OverviewList[4][1] = df1.iloc[18,2]
    OverviewList[5][1] = df1.iloc[19,2]

    OverviewList[6][1] = df1.iloc[20,2]
    OverviewList[7][1] = df1.iloc[5,4]

    worksheet_overview.write("A1" , OverviewList[0][0], bold1)
    worksheet_overview.write("A2" , OverviewList[1][0], bold1)
    worksheet_overview.write("A3" , OverviewList[2][0], bold1)
    worksheet_overview.write("A4" , OverviewList[3][0], bold1)
    worksheet_overview.write("A5" , OverviewList[4][0], bold1)
    worksheet_overview.write("A6" , OverviewList[5][0], bold1)
    worksheet_overview.write("A7" , OverviewList[6][0], bold1)
    worksheet_overview.write("A8" , OverviewList[7][0], bold1)

    worksheet_overview.write("B1" , OverviewList[0][1])
    worksheet_overview.write("B2" , OverviewList[1][1])
    worksheet_overview.write("B3" , OverviewList[2][1])
    worksheet_overview.write("B4" , OverviewList[3][1])
    worksheet_overview.write("B5" , OverviewList[4][1])
    worksheet_overview.write("B6" , OverviewList[5][1])
    worksheet_overview.write("B7" , OverviewList[6][1])
    worksheet_overview.write("B8" , OverviewList[7][1])

    for col_num, width in enumerate([30,100], start=0):
        worksheet_overview.set_column(col_num, col_num, width)

    for i in range(20):
        worksheet_overview.set_row(i, 20)

    data_df.to_excel(writer, sheet_name="Data", index=False, startrow=-1, startcol=0)
    format1 = workbook.add_format({"bold": True, "align": "center", "border": 1}) 
    worksheet_data = writer.sheets["Data"]
    worksheet_data.write("A1", "Year", format1)
    worksheet_data.write("B1", "United Kingdom", format1)
    worksheet_data.write("C1", "France", format1)
    worksheet_data.write("D1", "Germany", format1)
    worksheet_data.write("E1", "Italy", format1)
    worksheet_data.write("F1", "Spain", format1)


    for col_num, width in enumerate([30, 30, 30, 30, 30, 30], start=0):
        worksheet_data.set_column(col_num, col_num, width)

    for i in range(45):
        worksheet_data.set_row(i, 20)

    workbook.define_name("United_Kingdom", "Data!$B$2:$B$44")
    workbook.define_name("France", "Data!$C$2:$C$44")
    workbook.define_name("Germany", "Data!$D$2:$D$44")
    workbook.define_name("Italy", "Data!$E$2:$E$44")
    workbook.define_name("Spain", "Data!$F$2:$F$44")
    
    worksheet_stadistics = workbook.add_worksheet("Stadistics")
    format2=workbook.add_format({"bold": True, "align": "center"}) 

    #Mean
    worksheet_stadistics.write("A2", "Mean",bold1)
    worksheet_stadistics.write_formula("B2", "=AVERAGE('Data'!United_Kingdom)")
    worksheet_stadistics.write_formula("C2", "=AVERAGE('Data'!France)")
    worksheet_stadistics.write_formula("D2", "=AVERAGE('Data'!Germany)")
    worksheet_stadistics.write_formula("E2", "=AVERAGE('Data'!Italy)")
    worksheet_stadistics.write_formula("F2", "=AVERAGE('Data'!Spain)")

    #Min
    worksheet_stadistics.write("A3", "Minimum", bold1)
    worksheet_stadistics.write_formula("B3", "=MIN('Data'!United_Kingdom)")
    worksheet_stadistics.write_formula("C3", "=MIN('Data'!France)")
    worksheet_stadistics.write_formula("D3", "=MIN('Data'!Germany)")
    worksheet_stadistics.write_formula("E3", "=MIN('Data'!Italy)")
    worksheet_stadistics.write_formula("F3", "=MIN('Data'!Spain)")
    #Max
    worksheet_stadistics.write("A4", "Maximum", bold1)
    worksheet_stadistics.write_formula("B4", "=MAX('Data'!United_Kingdom)")
    worksheet_stadistics.write_formula("C4", "=MAX('Data'!France)")
    worksheet_stadistics.write_formula("D4", "=MAX('Data'!Germany)")
    worksheet_stadistics.write_formula("E4", "=MAX('Data'!Italy)")
    worksheet_stadistics.write_formula("F4", "=MAX('Data'!Spain)")


    worksheet_stadistics.write("A1", "Stadistics by Country", format2)
    worksheet_stadistics.write("B1", "United Kingdom", format2)
    worksheet_stadistics.write("C1", "France", format2)
    worksheet_stadistics.write("D1", "Germany", format2)
    worksheet_stadistics.write("E1", "Italy", format2)
    worksheet_stadistics.write("F1", "Spain", format2)

    for col_num, width in enumerate([30, 30, 30, 30, 30, 30], start=0):
        worksheet_stadistics.set_column(col_num, col_num, width)

    for i in range(4):
        worksheet_stadistics.set_row(i, 20)