import { useState } from 'react';
import './style.css'; 
import axios from 'axios';

function App() {
  const [option, setOption] = useState("url");
  const [url, setUrl] = useState("");
  const [file, setFile] = useState(null);
  const [summary, setSummary] = useState("");

  // ✅ Change this to your actual backend URL when deployed
  const BACKEND_URL = "https://summarizer-backend-kc6t.onrender.com"; 
  // For EC2 use: const BACKEND_URL = "http://<your-ec2-ip>:8000";

  const handleSummarize = async () => {
    const formData = new FormData();

    try {
      let res;
      if (option === "url") {
        formData.append("url", url);
        res = await axios.post(`${BACKEND_URL}/summarize/url`, formData);
      } else {
        formData.append("file", file);
        res = await axios.post(`${BACKEND_URL}/summarize/pdf`, formData);
      }

      setSummary(res.data.summary);
    } catch (err) {
      setSummary("Error: " + (err.response?.data?.detail || err.message));
    }
  };

  return (
    <div style={{ padding: "2rem", maxWidth: "600px", margin: "0 auto",background: "linear-gradient(rgb(185, 191, 229) 7%,rgb(222, 214, 234) 50%,rgb(188, 203, 227) 100%)", borderRadius: "8px", boxShadow: "0 2px 10px rgba(0,0,0,0.1)" }}>
      <h2 style={{ textAlign: "center",fontFamily:'cursive', color: "rgb(20, 22, 81)" }}>📄 Website or PDF Summarizer</h2>

      <select style={{ borderRadius: "2vw", padding: "0.5rem",background: "rgb(190, 169, 189)"  }} value={option} onChange={e => setOption(e.target.value)}>
        <option value="url">Website URL</option>
        <option value="pdf">Upload PDF</option>
      </select>

      {option === "url" ? (
        <input
          type="text"
          placeholder="Enter URL"
          value={url}
          onChange={e => setUrl(e.target.value)}
          style={{ borderRadius: "1vw",width: "100%", marginTop: "1rem", padding: "0.5rem" }}
        />
      ) : (
        <input
          type="file"
          accept="application/pdf"
          onChange={e => setFile(e.target.files[0])}
          style={{ marginTop: "1rem" }}
        />
      )}

      <button 
        onClick={handleSummarize}
        style={{ borderRadius: "2vw",marginTop: "1rem", padding: "0.5rem 1rem" }}
      >
        Summarize
      </button>

      {summary && (
        <div style={{ marginTop: "2rem" }}>
          <h3>📝 Summary:</h3>
          <p>{summary}</p>
        </div>
      )}
    </div>
  );
}

export default App;
