# import streamlit as st
# import os
#
# class AssistantGUI:
#     def __init__(self, assistant):
#         self.assistant = assistant
#         self.messages = assistant.messages
#         self.employee_information = assistant.employee_information
#
#     def get_response(self, user_input):
#         return self.assistant.get_response(user_input)
#
#     def render_messages(self):
#         messages = self.messages
#
#         for message in messages:
#             if message["role"] == "user":
#                 st.chat_message("human").markdown(message["content"])
#             if message["role"] == "ai":
#                 st.chat_message("ai").markdown(message["content"])
#
#     def set_state(self, key, value):
#         st.session_state[key] = value
#
#     def render_user_input(self):
#
#         user_input = st.chat_input("Type here...", key="input")
#         if user_input and user_input != "":
#             st.chat_message("human").markdown(user_input)
#
#             response_generator = self.get_response(user_input)
#
#             with st.chat_message("ai"):
#                 response = st.write_stream(response_generator)
#
#             self.messages.append({"role": "user", "content": user_input})
#             self.messages.append({"role": "ai", "content": response})
#
#             self.set_state("messages", self.messages)
#
#     def render_employee_info(self):
#         info = self.employee_information
#
#         st.markdown("""
#             <style>
#                 .info-box {
#                     background-color: #f9f9f9;
#                     padding: 15px;
#                     border-radius: 10px;
#                     font-family: 'Segoe UI', sans-serif;
#                     font-size: 16px;
#                     line-height: 1.6;
#                 }
#                 .info-title {
#                     font-size: 20px;
#                     font-weight: bold;
#                     margin-bottom: 10px;
#                 }
#                 .info-label {
#                     font-weight: 600;
#                     color: #333;
#                 }
#             </style>
#         """, unsafe_allow_html=True)
#
#         st.markdown('<div class="info-box">', unsafe_allow_html=True)
#         st.markdown('<div class="info-title">Employee Profile</div>', unsafe_allow_html=True)
#
#         st.markdown(f"""
#             <div><span class="info-label">Name:</span> {info['name']} {info['lastname']}</div>
#             <div><span class="info-label">Email:</span> {info['email']}</div>
#             <div><span class="info-label">Phone:</span> {info['phone_number']}</div>
#             <div><span class="info-label">Position:</span> {info['position']}</div>
#             <div><span class="info-label">Department:</span> {info['department']}</div>
#             <div><span class="info-label">Location:</span> {info['location']}</div>
#             <div><span class="info-label">Hire Date:</span> {info['hire_date']}</div>
#             <div><span class="info-label">Supervisor:</span> {info['supervisor']}</div>
#             <div><span class="info-label">Salary:</span> ${info['salary']:,.2f}</div>
#             <div><span class="info-label">Skills:</span> {', '.join(info['skills'])}</div>
#         """, unsafe_allow_html=True)
#
#         st.markdown('</div>', unsafe_allow_html=True)
#
#     def render(self):
#
#         with st.sidebar:
#             logo_path = os.path.join("image", "logo2.png")
#             st.image(logo_path, use_column_width=True)
#             st.title("InnovateTech Solutions Assistant")
#
#             # st.subheader("Employee Information")
#             # st.write(self.employee_information)
#             self.render_employee_info()
#
#         self.render_messages()
#         self.render_user_input()
import streamlit as st
import os

class AssistantGUI:
    def __init__(self, assistant):
        self.assistant = assistant
        self.messages = assistant.messages
        self.employee_information = assistant.employee_information

    def get_response(self, user_input):
        return self.assistant.get_response(user_input)

    def render_messages(self):
        messages = self.messages

        # Inject custom CSS for chat styling
        st.markdown("""
            <style>
                .chat-container {
                    font-family: 'Segoe UI', sans-serif;
                    font-size: 16px;
                }
                .user-msg {
                    background-color: #cce5ff;
                    color: #003366;
                    padding: 10px;
                    border-radius: 10px;
                    margin: 5px 0;
                    text-align: right;
                    width: fit-content;
                    max-width: 80%;
                    margin-left: auto;
                }
                .bot-msg {
                    background-color: #f1f0f0;
                    color: #333;
                    padding: 10px;
                    border-radius: 10px;
                    margin: 5px 0;
                    text-align: left;
                    width: fit-content;
                    max-width: 80%;
                    margin-right: auto;
                }
            </style>
        """, unsafe_allow_html=True)

        st.markdown('<div class="chat-container">', unsafe_allow_html=True)

        for message in messages:
            if message["role"] == "user":
                st.markdown(f'<div class="user-msg">{message["content"]}</div>', unsafe_allow_html=True)
            elif message["role"] == "ai":
                st.markdown(f'<div class="bot-msg">{message["content"]}</div>', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

    def set_state(self, key, value):
        st.session_state[key] = value

    def render_user_input(self):
        user_input = st.chat_input("Type here...", key="input")
        if user_input and user_input.strip() != "":
            st.markdown(f'<div class="user-msg">{user_input}</div>', unsafe_allow_html=True)

            response_generator = self.get_response(user_input)

            with st.spinner("Assistant is typing..."):
                response = st.write_stream(response_generator)

            # st.markdown(f'<div class="bot-msg">{response}</div>', unsafe_allow_html=True)

            self.messages.append({"role": "user", "content": user_input})
            self.messages.append({"role": "ai", "content": response})

            self.set_state("messages", self.messages)

    def render_employee_info(self):
        info = self.employee_information

        st.markdown("""
            <style>
                .info-box {
                    background-color: #f9f9f9;
                    padding: 15px;
                    border-radius: 10px;
                    font-family: 'Segoe UI', sans-serif;
                    font-size: 16px;
                    line-height: 1.6;
                }
                .info-title {
                    font-size: 20px;
                    font-weight: bold;
                    margin-bottom: 10px;
                }
                .info-label {
                    font-weight: 600;
                    color: #333;
                }
            </style>
        """, unsafe_allow_html=True)

        st.markdown('<div class="info-box">', unsafe_allow_html=True)
        st.markdown('<div class="info-title">Employee Profile</div>', unsafe_allow_html=True)

        st.markdown(f"""
            <div><span class="info-label">Name:</span> {info['name']} {info['lastname']}</div>
            <div><span class="info-label">Email:</span> {info['email']}</div>
            <div><span class="info-label">Phone:</span> {info['phone_number']}</div>
            <div><span class="info-label">Position:</span> {info['position']}</div>
            <div><span class="info-label">Department:</span> {info['department']}</div>
            <div><span class="info-label">Location:</span> {info['location']}</div>
            <div><span class="info-label">Hire Date:</span> {info['hire_date']}</div>
            <div><span class="info-label">Supervisor:</span> {info['supervisor']}</div>
            <div><span class="info-label">Salary:</span> ${info['salary']:,.2f}</div>
            <div><span class="info-label">Skills:</span> {', '.join(info['skills'])}</div>
        """, unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

    def render(self):
        with st.sidebar:
            logo_path = os.path.join("image", "logo2.png")
            st.image(logo_path, use_column_width=True)
            st.title("InnovateTech Solutions Assistant")
            self.render_employee_info()

        self.render_messages()
        self.render_user_input()

