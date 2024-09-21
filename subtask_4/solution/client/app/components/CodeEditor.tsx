import { useState } from "react";
import { Light as SyntaxHighlighter } from 'react-syntax-highlighter';
import python from 'react-syntax-highlighter/dist/esm/languages/hljs/python';
import CodeMirror from "@uiw/react-codemirror";
import { python as pythonLang } from "@codemirror/lang-python";
import Button from "./Button";

// Register the Python language
SyntaxHighlighter.registerLanguage('python', python);

export default function CodeEditor() {
  const [editorContent, setEditorContent] = useState<string>("# hello world");
  const [codeOutput, setCodeOutput] = useState<string | undefined>();
  const [hasOutputError, setHasOutputError] = useState<boolean>(false);

  const handleEditorChange = (value: string) => {
    setEditorContent(value);
  };

  const handleRunCode = async () => {
    const res = await fetch("http://127.0.0.1:8000/run_code", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ code: editorContent }),
    });

    const json: CodeOutput = await res.json();

    if (json.success) {
      setCodeOutput(json.output);
      setHasOutputError(false);
    } else {
      setCodeOutput(json.error);
      setHasOutputError(true);
    }
  };

  const handleSubmitCode = async () => {
    const res = await fetch("http://127.0.0.1:8000/submit_code", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ code: editorContent }),
    });

    const json = await res.json();
    const code_output: CodeOutput = json.code_output;

    if (json.db_success) {
      setCodeOutput(code_output.output);
      setHasOutputError(false);
      alert("code saved!");
    } else {
      setCodeOutput(code_output.error);
      setHasOutputError(true);
      alert("code failed to save!");
    }
  };

  return (
    <div className="w-full grow relative z-10">
      <div className="flex flex-col items-stretch justify-self-start">
        <CodeMirror
          value={editorContent}
          height="40vh"  // Shrink the height of the editor
          theme="dark"
          extensions={[pythonLang()]}
          onChange={(value) => handleEditorChange(value)}
          className="rounded-editor"
          style={{ borderRadius: '15px', overflow: 'hidden' }}  // Inline style for rounded corners
        />
        <div className="min-w-full flex flex-row items-center justify-between">
          <Button text="Test Code" onClick={handleRunCode} className="rounded-button neon-text" />
          <Button text="Submit" onClick={handleSubmitCode} className="rounded-button neon-text" />
        </div>
        <div className="output-container">
          <textarea
            className="e-input rounded-textarea terminal-font"
            readOnly
            value={codeOutput || ""}
            placeholder="Output will be displayed here"
          />
        </div>
      </div>
    </div>
  );
}

type CodeOutput = {
  success: boolean;
  output: string;
  error: string;
};
