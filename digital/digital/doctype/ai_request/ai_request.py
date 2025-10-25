# Copyright (c) 2025, tharun and contributors
# For license information, please see license.txt

import frappe
from openai import OpenAI
from frappe.model.document import Document


class AIRequest(Document):
	pass

@frappe.whitelist()
def generate_response(prompt, docname):
    if not prompt or not docname:
        frappe.throw("Prompt and docname are required")
    doc = frappe.get_doc("AI Request", docname)
    api_key = frappe.get_conf().get("openai_api_key")
    if not api_key:
        frappe.throw("OpenAI API key not found in site_config.json")
    client = OpenAI(api_key=api_key)
    try:
        res = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "system", "content": "You are a helpful assistant."},
                      {"role": "user", "content": prompt}],
            max_tokens=300
        )
        ai_msg = res.choices[0].message.content
        doc.response = (doc.response or "") + f"\n\nUser: {prompt}\nAI: {ai_msg}"
        doc.save()
        return ai_msg
    except Exception as e:
        frappe.log_error(f"AI Error: {str(e)}", "AI Request Error")
        return f"Error generating response: {str(e)}"