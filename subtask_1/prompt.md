# Subtask 1: Basic Frontend Setup with Code Editor

### Objective:
Set up a basic frontend application with a code editor component that allows users to write Python code.

---

### Requirements:

1. **Initialize a React project** using **Create React App** or **Next.js**.

2. **Install dependencies**:
    - Install React and React DOM.
    - Install **CodeMirror** for the code editor functionality. Use `@uiw/react-codemirror` and `@codemirror/lang-python` for React integration and Python syntax highlighting.

3. **Create a CodeEditor component** that:
    - Renders a code editor with **Python syntax highlighting**.
    - Uses **CodeMirror** for the code editor.
    - Initializes with the text `# Write your Python code here`.

4. **Set up the main application** to:
    - Render the **CodeEditor** component.
    - Ensure that the application runs without errors.

5. **No backend integration** is required at this stage.

---

### File Structure:

```bash
client/
  app/
  components/
    CodeEditor.js (or .tsx)
package.json
```

---

### Instructions:

- Do not include any global CSS or additional layout components at this stage.
- Focus only on setting up the code editor with **Python syntax highlighting**.
- Ensure that the application can run independently with `npm start` (or `npm run dev` if using Next.js).
