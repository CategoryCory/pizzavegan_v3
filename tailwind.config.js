const colors = require("tailwindcss/colors");

module.exports = {
  purge: [
      "{articles,home,pages,pizzavegan,pizzerias,products,recipes,search,templates}/**/*.html",
      "contacts/forms.py"
  ],
  darkMode: false, // or 'media' or 'class'
  theme: {
    fontFamily: {
      "sans": ["Jost", "ui-sans-serif", "system-ui", "-apple-system", "BlinkMacSystemFont", '"Segoe UI"', "Roboto", '"Helvetica Neue"', "Arial", '"Noto Sans"', "sans-serif", '"Apple Color Emoji"', '"Segoe UI Emoji"', '"Segoe UI Symbol"', '"Noto Color Emoji"'],
      "serif": ["Lora", "ui-serif", "Georgia", "Cambria", '"Times New Roman"', "Times", "serif"]
    },
    extend: {
      colors: {
        brand: {
          // DEFAULT: "#5eae46",
          // light: "#72c25a",
          // dark: "#4a9a32"
          // DEFAULT: "#BC150C",
          // light: "#D62F26",
          // dark: "#980B09"
          DEFAULT: "#B45A7E",
          light: "#C86E92",
          dark: "#9B4165"
        },
        secondary: {
          DEFAULT: "#3fa649",
          light: "#53BA5D",
          dark: "#2B9235"
        },
        gray: colors.warmGray,
      },
      typography: {
        brand: {
          css: {
            a: {
              color: "#B45A7E",
              "&:hover": {
                color: "#9B4165"
              }
            }
          }
        }
      }
    },
  },
  variants: {
    extend: {},
  },
  plugins: [
      require("@tailwindcss/typography"),
      require("@tailwindcss/forms")
  ],
}
