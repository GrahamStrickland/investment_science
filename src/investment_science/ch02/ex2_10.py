INVESTMENT = 1_000_000.0
RESERVES = 200_000.0
TAX_RATE = 0.45

BARRELS_PRODUCED = [80_000.0, 70_000.0, 50_000.0, 30_000.0, 10_000.0]
GROSS_REVENUE = [1_600_000.0, 1_400_000.0, 1_000_000.0, 600_000.0, 200_000.0]
NET_INCOME = [1_200_000.0, 1_000_000.0, 500_000.0, 200_000.0, 50_000.0]

Table = dict[str, list[float]]


def depletion_allowance_opt1(gross_revenue: float, net_income: float) -> float:
    """22% of gross revenue, up to 50% of net income."""
    return min(0.22 * gross_revenue, 0.5 * net_income)


def depletion_allowance_opt2(barrels_produced: float) -> float:
    """The investment cost times the fraction of the reserves produced, i.e.,
    $5 per barrel."""
    return barrels_produced * INVESTMENT / RESERVES


def table(depletion_allowance: list[float]) -> Table:
    taxable_income = [
        NET_INCOME[i] - depletion_allowance[i] for i in range(len(NET_INCOME))
    ]
    tax = [income * TAX_RATE for income in taxable_income]

    return {
        "barrels_produced": BARRELS_PRODUCED,
        "gross_revenue": GROSS_REVENUE,
        "net_income": NET_INCOME,
        "depletion_allowance": depletion_allowance,
        "taxable_income": taxable_income,
        "tax": tax,
        "after_tax_income": [NET_INCOME[i] - tax[i] for i in range(len(NET_INCOME))],
    }


def option1() -> Table:
    return table(
        [
            depletion_allowance_opt1(GROSS_REVENUE[i], NET_INCOME[i])
            for i in range(len(NET_INCOME))
        ]
    )


def option2() -> Table:
    return table([depletion_allowance_opt2(barrels) for barrels in BARRELS_PRODUCED])


def print_table(opt: Table) -> None:
    """Print the year followed by the columns calculated in table()."""
    columns = ["depletion_allowance", "taxable_income", "tax", "after_tax_income"]
    for year in range(len(NET_INCOME)):
        print(year + 1, *(f"{opt[column][year]:>9,.0f}" for column in columns))


def cash_flows(opt: Table) -> list[float]:
    """The initial investment followed by the after-tax income of each year."""
    return [-INVESTMENT] + opt["after_tax_income"]
