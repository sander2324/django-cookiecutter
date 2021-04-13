module.exports = {
  extends: [
    // Use the Airbnb style guide as base
    // Read more: https://github.com/airbnb/javascript
    'airbnb-base',
  ],
  parserOptions: {
    parser: 'babel-eslint',
  },
  env: {
    browser: true,
    es6: true,
    node: true,
  },
  ignorePatterns: ['frontend/config/**', '**/dist/**'],
  rules: {
    // Allow the use of console.log
    'no-console': 'off',
  },
};
