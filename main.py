from prettytable import PrettyTable
import argparse

def main(part, val, periods):
    history = {'0': val}
    for period in range(1, periods+1):
        val += val*part
        history[f"{period}"] = val
    return history

def renderTable(history, part):
    table = PrettyTable()
    table.field_names = ["Periods", f"Tatal sum increasing {part}", "Profit you achieve if you save the money"]
    data = []

    prevSum = history['0']
    for period in history.keys():
        data.append([period, f"{history[period]:.4f}", f"{history[period]-prevSum:.4f}"])
        prevSum = history[period]
    for row in data: table.add_row(row)

    # Print the table in string format
    print(table.get_string())

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="The module is to calculate several periods according to percent and a value.")
    parser.add_argument("--part", help="The part of the value which you can calculate the percent with. For instance, you can set it 0.2 (the number is between 0 and 1)")
    parser.add_argument("--val", help="The initial value as integer.")
    parser.add_argument("--periods", help="The number of periods that must be calculated.")
    args = parser.parse_args()

    renderTable( main(float(args.part), float(args.val), int(args.periods)), args.part  )
