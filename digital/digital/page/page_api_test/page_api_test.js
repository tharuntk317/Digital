frappe.pages['page-api-test'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Page API Test',
		single_column: true
	});
}
