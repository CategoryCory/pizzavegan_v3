const colors = require("tailwindcss/colors");

module.exports = {
  purge: [
      "{articles,home,pages,pizzavegan,pizzerias,products,recipes,search,templates}/**/*.html"
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
          DEFAULT: "#5eae46",
          light: "#72c25a",
          dark: "#4a9a32"
        },
        gray: colors.warmGray,
      },
      typography: {
        brand: {
          css: {
            a: {
              color: "#5eae46",
              "&:hover": {
                color: "#4a9a32"
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
