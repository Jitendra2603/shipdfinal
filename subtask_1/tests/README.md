To run the test in a **Next.js project with TypeScript** using Jest and React Testing Library, follow these steps:

### 1. Install the necessary dependencies

If you haven't already, install Jest, React Testing Library, and the necessary TypeScript testing types:

```bash
npm install --save-dev jest @testing-library/react @testing-library/jest-dom @testing-library/user-event ts-jest @types/jest
```

### 2. Set up Jest in your Next.js project

In the root of your project, create a file called `jest.config.js`:

```javascript
// jest.config.js
const nextJest = require("next/jest");

const createJestConfig = nextJest({
  dir: "./",
});

const customJestConfig = {
  setupFilesAfterEnv: ["<rootDir>/jest.setup.js"],
  testEnvironment: "jsdom",
};

module.exports = createJestConfig(customJestConfig);
```

### 3. Create a Jest setup file

Create a `jest.setup.js` file in the root of your project. This file is used to set up the testing environment, such as importing `@testing-library/jest-dom` to extend Jest matchers:

```javascript
// jest.setup.js
import '@testing-library/jest-dom/extend-expect';
```

### 4. Add a test script to `package.json`

Add a test script to your `package.json` to run the tests easily:

```json
{
  "scripts": {
    "test": "jest"
  }
}
```


### 5. Run the tests

To run the tests, use the following command in your terminal:

```bash
npm run test
```

