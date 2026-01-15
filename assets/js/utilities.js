const defaulStyle = {
    table: "margin: 0;",
    firstCol: {
        width: '60px',
        'text-align': 'center',
    },
    col: {
        width: '60px',
        'text-align': 'center',
        border: '#333 solid 1px'
    },
    styles: []
};

function draw_table(tablename, values, startindex, styles = defaulStyle) {
    document.writeln("<table class=\"draw-table\"",
        (styles.table) ? ("style=\"" + styles.table + "\"") : "", ">");
    document.writeln("<tr>");
    if (tablename) {
        document.writeln("<td style=\"", getStyle((styles.firstCol != null) ? styles.firstCol : {}), "\">", tablename, "</td>");
    }
    let i = 0;
    for (let v of values) {
        document.writeln("<td style=\"", getStyle(styles.col), getStyle((styles.styles && styles.styles[i]) ? styles.styles[i] : {}), "\">", v, "</td>");
        i++;
    }
    document.writeln("</tr>");
    document.writeln("<tr>");
    if (tablename) {
        document.writeln("<td><small>&nbsp;</small></td>");
    }
    for (let i = 0; i < values.length; i++) {
        document.writeln("<td style=\"text-align: center;\"><small>", i + startindex, "</small></td>");
    }
    document.writeln("</tr>");
    document.writeln("</table>");
}

function getStyle(styleObj) {
    if (styleObj == null) {
        styleObj = {};
    }
    return Object.keys(styleObj).map(key => key + ": " + styleObj[key] + ";").reduce((pv, cv) => pv + " " + cv, "").trim();
}

function DrawTableNoIndices(tablename, values, startindex, styles = {}) {
    document.writeln("<table class=\"draw-table\"",
        (styles.table) ? ("style=\"" + styles.table + "\"") : "", ">");
    document.writeln("<tr>");
    if (tablename) {
        document.writeln("<td style=\"", getStyle((styles.firstCol != null) ? styles.firstCol : {}), "\">", tablename, "</td>");
    }
    let i = 0;
    for (let v of values) {
        document.writeln("<td style=\"", getStyle(styles.col), getStyle((styles.styles && styles.styles[i]) ? styles.styles[i] : {}), "\">", v, "</td>");
        i++;
    }
    document.writeln("</tr>");
    document.writeln("</table>");
}