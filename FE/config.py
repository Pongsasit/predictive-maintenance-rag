watsonx_assistant_html_old = """
<script>
  window.watsonAssistantChatOptions = {
    integrationID: "6b79b14f-602b-445b-9adf-4bea809cd7eb", // The ID of this integration.
    region: "us-south", // The region your integration is hosted in.
    serviceInstanceID: "2a4f2d74-9c3a-42af-a962-af18dc97dadf", // The ID of your service instance.
    onLoad: async (instance) => { await instance.render(); }
  };
  setTimeout(function(){
    const t=document.createElement('script');
    t.src="https://web-chat.global.assistant.watson.appdomain.cloud/versions/" + (window.watsonAssistantChatOptions.clientVersion || 'latest') + "/WatsonAssistantChatEntry.js";
    document.head.appendChild(t);
  });
</script>
    """
visualizaer_url = 'https://th-tmg-graph-gen-frontend.1fk6set215qw.jp-tok.codeengine.appdomain.cloud'


watsonx_assistant_html = """
<script>
  window.watsonAssistantChatOptions = {
    integrationID: "b5a2edcf-c502-498b-a1de-b5b8d27ab6b1", // The ID of this integration.
    region: "us-south", // The region your integration is hosted in.
    serviceInstanceID: "1696a773-e32d-44c6-9b26-c2d38d5adad9", // The ID of your service instance.
    onLoad: async (instance) => { await instance.render(); }
  };
  setTimeout(function(){
    const t=document.createElement('script');
    t.src="https://web-chat.global.assistant.watson.appdomain.cloud/versions/" + (window.watsonAssistantChatOptions.clientVersion || 'latest') + "/WatsonAssistantChatEntry.js";
    document.head.appendChild(t);
  });
</script>
"""