frappe.ui.form.on('Purchase Order', {
    refresh: function(frm) {
        // Render the custom table using the child table data
        frappe.call({
            method: "frappe.client.get_list",
            args: {
                doctype: "Custom Purchase Order Item",
                filters: { parent: frm.doc.name },
                fields: ["item_code", "date", "description", "qty", "rate", "amount", "uom", "invoice", "order", "payment", "note", "column_name_1"]
            },
            callback: function(response) {
                let rows = response.message || [];
                let html = frappe.render_template('custom_child_table', { rows: rows });
                frm.fields_dict.custom_child_table_html.$wrapper.html(html);

                // Add event listener for in-place editing
                frm.fields_dict.custom_child_table_html.$wrapper.find('input').on('change', function(e) {
                    let field = $(this).data('field');
                    let value = $(this).val();
                    let rowIndex = $(this).closest('tr').data('row-index');
                    
                    // Update the respective child table row
                    if (frm.doc.custom_custom_purchase_order_item && frm.doc.custom_custom_purchase_order_item[rowIndex]) {
                        frm.doc.custom_custom_purchase_order_item[rowIndex][field] = value;
                    }
                });
            }
        });
    }
});
