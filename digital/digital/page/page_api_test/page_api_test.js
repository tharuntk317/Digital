frappe.pages['page-api-test'].on_page_load = function(wrapper) {
    var page = frappe.ui.make_app_page({
        parent: wrapper,
        title: 'Review Page',
        single_column: true
    });
    $(frappe.render_template(`
        <div style="padding: 20px;">
            <h3> Review Summary Report</h3>
            <p>Welcome to the Review Page! Here you can view the latest feedback, ratings, and analysis summary of your products or services.</p>
            <ul>
                <li><b>Total Reviews:</b> <span id="total-reviews">0</span></li>
                <li><b>Average Rating:</b>  <span id="avg-rating">0</span> / 5</li>
                <li><b>Most Recent Reviewer:</b> <span id="recent-reviewer">-</span></li>
            </ul>
            <p style="color: gray;">Last updated: ${frappe.datetime.now_datetime()}</p>
        </div>
        <div id="review-chart"></div>
    `)).appendTo(page.body);

    let lastWeek = frappe.datetime.add_days(frappe.datetime.nowdate(), -7);

    frappe.call({
        method: "frappe.client.get_list",
        args: {
            doctype: "Review Page",
            fields: ["product", "make_star", "feedback", "review_date"],
            filters: [["review_date", ">", lastWeek]],
            limit_page_length: 100
        },
        callback: function(r) {
            if (r.message) {
                let data = r.message;
                $("#total-reviews").text(data.length);

                if(data.length > 0){
                    let avg = (data.reduce((sum, d) => sum + (d.make_star || 0), 0) / data.length).toFixed(1);
                    $("#avg-rating").text(avg);
                    $("#recent-reviewer").text(data[data.length - 1].product); 
                }
                let productMap = {};
                data.forEach(d => {
                    if(!productMap[d.product]) productMap[d.product] = [];
                    productMap[d.product].push(d.make_star || 0);
                });

                let labels = Object.keys(productMap);
                let stars = labels.map(p => {
                    let arr = productMap[p];
                    return (arr.reduce((a,b) => a+b,0) / arr.length).toFixed(1);
                });
                new frappe.Chart("#review-chart", {
                    title: "Average Star Rating per Product (Last 7 Days)",
                    data: {
                        labels: labels,
                        datasets: [
                            {
                                name: "Stars",
                                type: "pie",
                                values: stars
                            }
                        ]
                    },
                    type: 'pie',
                    height: 300,
                    colors: ['blue']
                });
            }
        }
    });
let $btn = page.set_primary_action('GO TO HOME', () => {
    frappe.set_route('/app');
});

};


 