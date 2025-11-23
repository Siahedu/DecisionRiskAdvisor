import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Watsonx Orchestrate Chat Demo", layout="wide")

st.title("Watsonx Orchestrate Chat UI Demo in Streamlit")

st.write("### Debug Info")
st.write("If you see this but no chat UI below, check the browser console (F12) for logs.")
st.write("Look for: 'Initializing watsonx Orchestrate chat...', 'wxoLoader initialized', etc.")

html_code = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body, html {
            margin: 0;
            padding: 0;
            height: 100%;
            width: 100%;
        }
        #root {
            width: 100%;
            height: 100%;
            min-height: 600px;
        }
    </style>
</head>
<body>
    <div id="root" style="background-color: #f0f0f0; border: 2px solid red;">
        <p style="padding: 20px;">Loading chat widget... If you see this text, the div exists but chat hasn't rendered.</p>
    </div>

    <script>
      console.log('=== WATSONX ORCHESTRATE DEBUG START ===');
      console.log('1. Initializing watsonx Orchestrate chat...');
      console.log('2. Root element exists:', document.getElementById('root'));

      window.wxOConfiguration = {
        orchestrationID: "7629ddb4155d4c74870dfe485de0f4f4_b8a5b2db-cea0-462e-9710-31ab94803f7f",
        hostURL: "https://us-south.watson-orchestrate.cloud.ibm.com",
        rootElementID: "root",
        deploymentPlatform: "ibmcloud",
        crn: "crn:v1:bluemix:public:watsonx-orchestrate:us-south:a/7629ddb4155d4c74870dfe485de0f4f4:b8a5b2db-cea0-462e-9710-31ab94803f7f::",
        chatOptions: {
            agentId: "8a70f907-9c04-43bf-868d-6095fb400c88",
            agentEnvironmentId: "2a460464-b9b2-4903-b22d-462d7e32f9a2"
        },
        layout: {
            form: "float",
            width: "100%",
            height: "600px"
        }
      };

      console.log('3. Configuration set:', JSON.stringify(window.wxOConfiguration, null, 2));

      setTimeout(function () {
        console.log('4. Loading wxoLoader script from:', window.wxOConfiguration.hostURL + '/wxochat/wxoLoader.js?embed=true');
        const script = document.createElement('script');
        script.src = window.wxOConfiguration.hostURL + '/wxochat/wxoLoader.js?embed=true';

        script.addEventListener('load', function () {
            console.log('5. wxoLoader script LOADED successfully');
            console.log('6. wxoLoader available?', typeof wxoLoader !== 'undefined');
            console.log('7. wxoLoader object:', wxoLoader);

            if (typeof wxoLoader !== 'undefined') {
                console.log('8. Calling wxoLoader.init()...');
                try {
                    wxoLoader.init();
                    console.log('9. wxoLoader.init() completed successfully');

                    // Check what got rendered
                    setTimeout(function() {
                        const rootEl = document.getElementById('root');
                        console.log('11. Root element after init:', rootEl);
                        console.log('12. Root element innerHTML:', rootEl.innerHTML);
                        console.log('13. Root element children count:', rootEl.children.length);
                        if (rootEl.children.length > 0) {
                            console.log('14. First child:', rootEl.children[0]);
                        } else {
                            console.warn('WARNING: No children rendered in root element!');
                        }
                    }, 2000);
                } catch (error) {
                    console.error('ERROR during wxoLoader.init():', error);
                }
            } else {
                console.error('ERROR: wxoLoader is undefined after script load');
            }
        });

        script.addEventListener('error', function(e) {
            console.error('ERROR: Failed to load wxoLoader script:', e);
        });

        document.head.appendChild(script);
        console.log('10. Script tag appended to head');
      }, 500);
    </script>
</body>
</html>
"""

components.html(html_code, height=700, scrolling=False, width=None)
