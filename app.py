import os
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "super-secret-key-12345")

# Mock Servers Data for Bot Management
SERVERS_DATA = [
    {
        "id": "1001",
        "name": "CyberVerse Official",
        "icon": "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=150&auto=format&fit=crop&q=80",
        "members": 14200,
        "active_tickets": 12,
        "status": "Online",
        "config": {
            "ticket_category": "Tickets Area",
            "support_role": "@Ticket Support",
            "welcome_msg": "สวัสดีครับ! กรุณาระบุรายละเอียดปัญหาของคุณ",
            "auto_close": "24 ชั่วโมง",
            "max_tickets": 3,
            "transcript_log": "#ticket-logs",
            "modal_form": True,
            "claiming_system": True,
            "rating_system": True,
            "working_hours": "09:00 - 22:00"
        }
    },
    {
        "id": "1002",
        "name": "Aetherium Esports",
        "icon": "https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=150&auto=format&fit=crop&q=80",
        "members": 8900,
        "active_tickets": 5,
        "status": "Online",
        "config": {
            "ticket_category": "Support Center",
            "support_role": "@Mod Team",
            "welcome_msg": "ทีมงานจะตอบกลับภายใน 15 นาที",
            "auto_close": "12 ชั่วโมง",
            "max_tickets": 1,
            "transcript_log": "#support-transcripts",
            "modal_form": True,
            "claiming_system": False,
            "rating_system": True,
            "working_hours": "24 ชั่วโมง"
        }
    },
    {
        "id": "1003",
        "name": "Nexus Roleplay TH",
        "icon": "https://images.unsplash.com/photo-1542751371-adc38448a05e?w=150&auto=format&fit=crop&q=80",
        "members": 23500,
        "active_tickets": 28,
        "status": "Online",
        "config": {
            "ticket_category": "Helpdesk",
            "support_role": "@Admin Staff",
            "welcome_msg": "กรุณาเตรียมภาพถ่ายหรือคลิปวิดีโอหลักฐานให้พร้อม",
            "auto_close": "48 ชั่วโมง",
            "max_tickets": 5,
            "transcript_log": "#admin-logs",
            "modal_form": True,
            "claiming_system": True,
            "rating_system": False,
            "working_hours": "10:00 - 02:00"
        }
    }
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/servers")
def get_servers():
    return jsonify({"success": True, "servers": SERVERS_DATA})

@app.route("/api/server/<server_id>/save", methods=["POST"])
def save_config(server_id):
    data = request.json
    for server in SERVERS_DATA:
        if server["id"] == server_id:
            server["config"].update(data)
            return jsonify({"success": True, "message": "บันทึกการตั้งค่าระบบทิกเก็ตเรียบร้อยแล้ว!"})
    return jsonify({"success": False, "message": "ไม่พบเซิร์ฟเวอร์"}), 404

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
