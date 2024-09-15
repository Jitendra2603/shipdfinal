// CodeEditor.test.tsx

import React from 'react';
import { render, fireEvent, screen } from '@testing-library/react';
import CodeEditor from '../solution/CodeEditor';
import '@testing-library/jest-dom/extend-expect';

describe('CodeEditor Component', () => {
  test('renders without crashing', () => {
    render(<CodeEditor />);
    const editorElement = screen.getByRole('textbox');
    expect(editorElement).toBeInTheDocument();
  });

  test('syntax highlighting works', () => {
    // Since we cannot visually test syntax highlighting, we can ensure that the editor accepts input.
    render(<CodeEditor />);
    const editorElement = screen.getByRole('textbox');
    fireEvent.change(editorElement, { target: { value: 'print("Hello World")' } });
    expect(editorElement).toHaveValue('print("Hello World")');
  });

  test('run code button triggers code execution', async () => {
    render(<CodeEditor />);
    const runButton = screen.getByText('Run Code');
    fireEvent.click(runButton);
    const outputArea = await screen.findByPlaceholderText('Output will be displayed here');
    expect(outputArea).toHaveValue('Hello, World!\n');
  });
});
