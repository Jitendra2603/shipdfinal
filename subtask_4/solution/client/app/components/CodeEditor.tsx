"use client";

import React, { useState } from "react";
import CodeMirror from "@uiw/react-codemirror";
import { python } from "@codemirror/lang-python";
import Button from "./Button";

export default function CodeEditor() {
  const [code, setCode] = useState<string>("# Write your Python code here");
  const [output, setOutput] = useState<string>("");
  const [hasError, setHasError] = useState<boolean>(false);

  const handleRunCode = async () => {
    const payload = { code };
    try {
      const response = await fetch("http://localhost:8000/run_code", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });
      const data = await response.json();
      if (data.success) {
        setOutput(data.output);
        setHasError(false);
      } else {
        setOutput(data.error);
        setHasError(true);
      }
    } catch (error) {
      setOutput("Error connecting to backend API.");
      setHasError(true);
    }
  };

  const handleSubmitCode = async () => {
    const payload = { code };
    try {
      const response = await fetch("http://localhost:8000/submit_code", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });
      const data = await response.json();
      if (data.db_success) {
        setOutput(data.code_output.output);
        setHasError(false);
        alert("Code saved successfully!");
      } else {
        setOutput(data.code_output.error || data.error);
        setHasError(true);
        alert("Code execution failed. Not saved.");
      }
    } catch (error) {
      setOutput("Error connecting to backend API.");
      setHasError(true);
    }
  };

  return (
    <div className="w-full grow relative z-10">
      <div className="flex flex-col items-stretch justify-self-start">
        <CodeMirror
          value={code}
          height="40vh"
          theme="dark"
          extensions={[python()]}
          onChange={(value) => setCode(value)}
          className="rounded-editor"
          style={{ borderRadius: "15px", overflow: "hidden" }}
        />
        <div className="min-w-full flex flex-row items-center justify-between">
          <Button text="Run Code" onClick={handleRunCode} className="rounded-button neon-text" />
          <Button text="Submit Code" onClick={handleSubmitCode} className="rounded-button neon-text" />
        </div>
        <div className="output-container">
          <textarea
            className={`e-input rounded-textarea terminal-font ${hasError ? "error" : ""}`}
            readOnly
            value={output}
            placeholder="Output will be displayed here"
          />
        </div>
      </div>
    </div>
  );
}

