import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Watsonx Orchestrate Chat Demo", layout="wide")

st.title("Watsonx Orchestrate Chat UI Demo - Custom Layout")

st.write("### Debug Info")
st.write("This version uses proper DOM element reference for custom layout.")

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
            background-color: #f5f5f5;
            border: 2px solid #ccc;
        }
    </style>
</head>
<body>
    <div id="root"></div>

    <script>
      console.log('=== WATSONX ORCHESTRATE CUSTOM LAYOUT DEBUG ===');
      console.log('1. Getting root element...');

      const rootElement = document.getElementById('root');
      console.log('2. Root element:', rootElement);

      window.wxOConfiguration = {
        orchestrationID: "7629ddb4155d4c74870dfe485de0f4f4_b8a5b2db-cea0-462e-9710-31ab94803f7f",
        hostURL: "https://us-south.watson-orchestrate.cloud.ibm.com",
        element: rootElement,  // Pass actual element instead of ID
        deploymentPlatform: "ibmcloud",
        crn: "crn:v1:bluemix:public:watsonx-orchestrate:us-south:a/7629ddb4155d4c74870dfe485de0f4f4:b8a5b2db-cea0-462e-9710-31ab94803f7f::",
        chatOptions: {
            agentId: "8a70f907-9c04-43bf-868d-6095fb400c88",
            agentEnvironmentId: "2a460464-b9b2-4903-b22d-462d7e32f9a2"
        },
        layout: {
            form: "custom",
            showHeader: true
        }
      };

      console.log('3. Configuration with element:', window.wxOConfiguration);

      setTimeout(function () {
        console.log('4. Loading wxoLoader script...');
        const script = document.createElement('script');
        script.src = window.wxOConfiguration.hostURL + '/wxochat/wxoLoader.js?embed=true';

        script.addEventListener('load', function () {
            console.log('5. wxoLoader loaded');
            if (typeof wxoLoader !== 'undefined') {
                console.log('6. Calling wxoLoader.init()...');
                try {
                    wxoLoader.init();
                    console.log('7. Init completed');

                    setTimeout(function() {
                        console.log('8. Root element after init:', rootElement);
                        console.log('9. Children count:', rootElement.children.length);
                    }, 2000);
                } catch (error) {
                    console.error('ERROR during init:', error);
                }
            }
        });

        script.addEventListener('error', function(e) {
            console.error('ERROR loading script:', e);
        });

        document.head.appendChild(script);
      }, 500);
    </script>
</body>
</html>
"""

components.html(html_code, height=700, scrolling=False, width=None)
