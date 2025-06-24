import { useState } from 'react';
import './style.css';
import axios from 'axios';

function App() {
  const [option, setOption] = useState("url");
  const [url, setUrl] = useState("");
  const [file, setFile] = useState(null);
  const [summary, setSummary] = useState("");

  const BACKEND_URL = "http://ec2-16-171-19-9.eu-north-1.compute.amazonaws.com:8000";

  const handleSummarize = async () => {
    try {
      let res;
      if (option === "url") {
        res = await axios.post(`${BACKEND_URL}/summarize-url`, { url });
      } else {
        const formData = new FormData();
        formData.append("file", file);
        res = await axios.post(`${BACKEND_URL}/summarize-pdf`, formData, {
          headers: { "Content-Type": "multipart/form-data" }
        });
      }
      setSummary(res.data.summary);
    } catch (err) {
      setSummary("❌ Error: " + (err.response?.data?.detail || err.message));
    }
  };

  return (
    <div style={{ padding: "2rem", maxWidth: "600px", margin: "0 auto", background: "#f5f5ff", borderRadius: "8px" }}>
      <h2 style={{ textAlign: "center", fontFamily: 'cursive', color: "#141651" }}>📄 Website or PDF Summarizer</h2>
      <select value={option} onChange={e => setOption(e.target.value)}>
        <option value="url">Website URL</option>
        <option value="pdf">Upload PDF</option>
      </select>
      {option === "url" ? (
        <input type="text" value={url} onChange={e => setUrl(e.target.value)} placeholder="Enter website URL" />
      ) : (
        <input type="file" accept="application/pdf" onChange={e => setFile(e.target.files[0])} />
      )}
      <button onClick={handleSummarize}>Summarize</button>
      {summary && (
        <div>
          <h3>📝 Summary:</h3>
          <p>{summary}</p>
        </div>
      )}
    </div>
  );
}

export default App;
