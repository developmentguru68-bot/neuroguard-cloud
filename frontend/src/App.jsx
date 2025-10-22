import React, { useState } from "react";

export default function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);

  const uploadFile = async () => {
    const formData = new FormData();
    formData.append("file", file);
    const res = await fetch("https://neuroguard-cloud.onrender.com/analyze", {
      method: "POST",
      body: formData,
    });
    const data = await res.json();
    setResult(data);
  };

  return (
    <div className="min-h-screen bg-slate-100 p-10 text-gray-800">
      <h1 className="text-4xl font-bold mb-6 text-blue-700">🧠 NeuroGuard Cloud</h1>
      <input
        type="file"
        onChange={(e) => setFile(e.target.files[0])}
        className="border p-2"
      />
      <button
        onClick={uploadFile}
        className="bg-blue-700 text-white px-4 py-2 rounded ml-2 hover:bg-blue-800"
      >
        Analyze
      </button>

      {result && (
        <div className="mt-4 p-4 bg-white shadow rounded">
          <p><b>Prediction:</b> {result.prediction}</p>
          <a
            href={`https://neuroguard-cloud.onrender.com${result.pdf_url}`}
            className="text-blue-600 underline"
            target="_blank"
          >
            Download Report
          </a>
        </div>
      )}
    </div>
  );
}


