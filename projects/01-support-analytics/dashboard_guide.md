# Optional Power BI Desktop walkthrough (free desktop application)

**Status:** instructions only; an actual `.pbix` report has not been built or validated. This is a **synthetic** operational dataset, unrelated to employer exports.

1. Install Power BI Desktop and import `data/support_tickets_synthetic.csv` using **Get Data → Text/CSV**.
2. Set timestamps as Date/Time; retain blanks as null. Check that exactly 60 tickets load, 48 closed and 12 open.
3. Create cards for ticket total, open/closed counts, observed first-view duration and closed-only mean resolution time.
4. Plot tickets opened by month and team; tickets closed by closure month; filtering by synthetic category.
5. To prevent denominator confusion, explicitly label metrics as `first view observed`, `closed cases only` and `assigned operators`.
6. Use a fixed observation date for snapshots rather than interpreting the computer's current date as the real historic analysis date.

Do not publish real employer dashboard code, internal schema, customer identifiers or personnel records.
