import React, { useState } from 'react';
import CodeMirror from '@uiw/react-codemirror';
import { python } from '@codemirror/lang-python';
import Button from './Button';

export default function CodeEditor() {
  const [code, setCode] = useState<string>('# Write your Python code here');
  const [output, setOutput] = useState<string>('');

  const handleRunCode = async () => {
    // Mock API response for testing
    const mockResponse = { output: 'Hello, World!\n', error: '', success: true };
    setOutput(mockResponse.output);
  };

  return (
    <div className="code-editor-container">
      <CodeMirror
        value={code}
        height="300px"
        extensions={[python()]}
        onChange={(value) => setCode(value)}
        className="code-mirror-editor"
      />
      <Button onClick={handleRunCode} text="Run Code" />
      <textarea
        readOnly
        value={output}
        placeholder="Output will be displayed here"
        className="output-area"
      />
    </div>
  );
}
