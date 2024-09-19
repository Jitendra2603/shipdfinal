# Hints for Subtask 1

1. **Slight Hint**:
   - Start by selecting a code editor library that integrates well with React. **CodeMirror** is a popular choice that offers extensive customization and syntax highlighting support for Python.

2. **Moderate Hint**:
   - Install the `@uiw/react-codemirror` package using npm or yarn. Configure the editor to use the Python language mode by importing and registering the Python extension from `@codemirror/lang-python`.
   - Example:
     ```javascript
     import CodeMirror from '@uiw/react-codemirror';
     import { python } from '@codemirror/lang-python';

     <CodeMirror
       extensions={[python()]}
       // other props
     />
     ```

3. **Strong Hint**:
   - Implement state management for the code input and output using React hooks (`useState`). Create handler functions for the "Run Code" and "Submit Code" buttons that send POST requests to the `/run_code` and `/submit_code` endpoints respectively.
   - Ensure that the responses from the backend are properly captured and displayed in the output area. Handle error scenarios by updating the output state with error messages.
   - Example:
     ```javascript
     const [code, setCode] = useState('');
     const [output, setOutput] = useState('');

     const handleRunCode = async () => {
       try {
         const response = await fetch('http://localhost:8000/run_code', {
           method: 'POST',
           headers: { 'Content-Type': 'application/json' },
           body: JSON.stringify({ code }),
         });
         const data = await response.json();
         setOutput(data.success ? data.output : `Error: ${data.error}`);
       } catch (error) {
         setOutput('Failed to connect to the backend API.');
       }
     };
     ```
