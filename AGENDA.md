# Welcome to Streamlit

**A faster way to build and share data apps.**

![logo](https://lh3.googleusercontent.com/-UU_-cM2FZnI/YLgc3z-EFCI/AAAAAAAAAuo/sORie7aJNgsM8UY7_qAUTZUSeSxKtA7UQCLcBGAsYHQ/s16000/streamlit_log.png)

# TABLE OF CONTENT 

1. [**Introduction**](#Introduction)
2. [**Basic components**](#Basic-components)
3. [**Data display elements**](#Data-display-elements)
4. [**Input widget elements**](#Input-widget-elements)
5. [**Chart elements**](#Chart-elements)
6. [**Status elements**](#Status-elements)
7. [**Download button**](#Download-button)
8. [**First App in streamlit**](#First-App-in-streamlit)
9. [**Streamlit with SQL server using SQLite3L**](#Streamlit-with-SQL-server-using-SQLite3L)
10. [**Login page**](#Login-page)
11. [**Deploy App to Streamlit Cloud**](#Deploy-App-to-Streamlit-Cloud)
12. [**Conclusion**](#Conclusion)
13. [**Reference**](#Reference)

## Introduction
- Streamlit is an open-source app framework that allows you to quickly build and deploy interactive, web-based applications for data exploration, machine learning, and more. With Streamlit, you can transform your Python scripts into shareable apps in minutes, without requiring any front-end development experience.

- Streamlit is designed to be simple and intuitive, with a focus on fast, interactive prototyping. It features live editing, so you can see your app update instantly as you edit your script. Streamlit is also open-source and free, with a vibrant community of contributors and users.

- To get started with Streamlit, you can install it using pip and run the `streamlit hello` command to see a demo app. From there, you can start building your own apps by importing the Streamlit library and using its various functions to display text, data, charts, and more.

- Streamlit supports a wide range of data visualization libraries, including Matplotlib, Altair, Plotly, Vega-Lite, Bokeh, and Pydeck. It also includes built-in functions for displaying data frames, tables, images, and text.

- In addition to data display elements, Streamlit provides a variety of input widgets, such as buttons, radio buttons, checkboxes, select boxes, multi-select boxes, sliders, text inputs, number inputs, text areas, and date/time inputs. These widgets allow users to interact with your app and provide input, which can then be used to generate dynamic, personalized content.

- Streamlit also includes features for managing app state, such as spinners, progress bars, informational messages, and empty placeholders. These elements can help you provide feedback to users and manage the flow of your app.

- To share your Streamlit apps with others, you can deploy them to the web using Streamlit's built-in sharing feature or by using a third-party hosting service. Streamlit also supports integration with SQL databases, allowing you to build apps that interact with your data directly.

- Overall, Streamlit is a powerful and flexible tool for building interactive, data-driven apps. Whether you're a data scientist, machine learning engineer, or developer, Streamlit can help you quickly create and share your work with others

### What is Streamlit?

Streamlit lets you transform Python scripts into interactive web apps in minutes, instead of weeks. Build dashboards, generate reports, or create chat apps. Once you’ve created an app, you can use our [Community Cloud platform](https://streamlit.io/cloud) to deploy, manage, and share your app.

### Why choose Streamlit?

- **Simple and Pythonic:** Write beautiful, easy-to-read code.
- **Fast, interactive prototyping:** Let others interact with your data and provide feedback quickly.
- **Live editing:** See your app update instantly as you edit your script.
- **Open-source and free:** Join a vibrant community and contribute to Streamlit's future.

### Installation

Open a terminal and run:

```bash
$ pip install streamlit
$ streamlit hello
```
If this opens our sweet _Streamlit Hello_ app in your browser, you're all set! If not, head over to [our docs](https://docs.streamlit.io/library/get-started) for specific installs.

## Basic components
- **Text:** Display text using `st.text()`, `st.title()`, `st.header()`, `st.subheader()`, `st.markdown()` functions. These functions allow you to display static text, headers, and formatted text using Markdown syntax.

  - **`st.text()`:** This function is used to display text on the Streamlit app. It can be used to show plain text, numbers, or any other non-formatted data.

  - **`st.title()`:** This function sets a title for your Streamlit app. It's typically used at the beginning of the app to provide a title that describes the purpose or content of the application.

  - **`st.header()`:** This function is used to create a header in your Streamlit app. Headers are larger and more visually prominent than regular text and can be used to organize and separate different sections of your app.

  - **`st.subheader()`:** Similar to `st.header()`, this function creates a subheader in your Streamlit app. Subheaders are smaller than headers but larger than regular text, making them useful for dividing content into subsections.

  - **`st.markdown()`:** This function allows you to render Markdown syntax within your Streamlit app. Markdown is a lightweight markup language that enables you to format text, create lists, include images, and more. `st.markdown()` lets you incorporate formatted text or even HTML code directly into your Streamlit app.

## Data display elements
- Streamlit makes it easy to display data such as data frames, images, and plots.

  - **`st.dataframe()`:** This function is used to display Pandas DataFrames within your Streamlit app. It automatically formats the DataFrame to fit nicely within the app and provides features such as sorting and searching.

  - **`st.table()`:** Similar to `st.dataframe()`, this function displays data in a table format. However, `st.table()` is more flexible and can display not only Pandas DataFrames but also lists, dictionaries, and other tabular data structures.

  - **`st.image()`:** This function is used t`o display images within your Streamlit app. You can pass either a URL or a file path to the image, and Streamlit will render it in the app.

  - **`st.pyplot()`, `st.altair_chart()`, `st.plotly_chart()`, `st.vega_lite_chart()`:** These functions are used to display plots created with various plotting libraries. Each function corresponds to a different plotting library (`matplotlib`, `Altair`, `Plotly`, and `Vega-Lite`, `respectively`). You pass the plot object created with the corresponding library's plotting functions, and Streamlit will render it within the app.


## Input widget elements

  - **`st.button()`:** This function creates a button widget. It returns `True` if the button was clicked, and `False` otherwise.

  - **`st.radio()`:** This function creates a radio button widget. It allows the user to select one option from a list of choices. It returns the selected choice as a string.

  - **`st.checkbox()`:** This function creates a checkbox widget. It allows the user to select multiple options from a list of choices. It returns a boolean value for each choice, indicating whether it is selected or not.

  - **`st.selectbox()`:** This function creates a dropdown select widget. It allows the user to select one option from a list of choices. It returns the selected choice as a string.

  - **`st.multiselect()`:** This function creates a multi-select widget. It allows the user to select multiple options from a list of choices. It returns a list of the selected choices.

  - **`st.slider()`:** This function creates a slider widget. It allows the user to select a value or range of values within a specified range. It returns the selected value(s) as a number or a tuple of numbers.

  - **`st.text_input()`:** This function creates a text input widget. It allows the user to enter text. It returns the entered text as a string.

  - **`st.number_input()`:** This function creates a numeric input widget. It allows the user to enter a number. It returns the entered number as a float or an integer.

  - **`st.text_area()`:** This function creates a text area widget. It allows the user to enter multiple lines of text. It returns the entered text as a string.

  - **`st.date_input()`, `st.time_input()`, `st.datetime_input()`:** These functions create date, time, and datetime input widgets, respectively. They allow the user to enter a date, time, or datetime. They return the entered value as a datetime object

## Chart elements 

1. [**Matplotlib Charts**](#Matplotlib-Charts)
2. [**Altair Charts**](#Altair-Charts)
3. [**Plotly Charts**](#Plotly-Charts)
4. [**Vega-Lite Charts**](#Vega-Lite-Charts)
5. [**Bokeh Charts**](#Bokeh-Charts)
6. [**Pydeck Charts**](#Pydeck-Charts)

### **Matplotlib Charts**

  1) **Create a Matplotlib Figure:** First, you need to create your Matplotlib figure as you would normally in Python. This involves importing Matplotlib and using its functions to create your desired plot.

  2) **Pass the Figure to `st.pyplot()`:** Once you have your Matplotlib figure object, you can pass it to the `st.pyplot()` function provided by Streamlit. This function takes the Matplotlib figure as its argument.

  3) **Display in Streamlit App:** When your Streamlit app runs and encounters the `st.pyplot()` function with your Matplotlib figure, it will render the figure directly within your Streamlit app. This allows your users to interact with and view the Matplotlib plot alongside other content in your app

### **Altair Charts**

You can create interactive Altair charts using the `st.altair_chart()` function. This function allows you to display Altair charts in your app.

  1) **Create an Altair Chart:** First, you need to create your Altair chart using Altair's Python API. This involves importing Altair and using its functions to define your chart's specifications, such as the data source, encoding (e.g., x-axis, y-axis), mark type (e.g., bar, line), and any additional customization.

  2) **Pass the Chart to `st.altair_chart()`:** Once you have your Altair chart object, you can pass it to the `st.altair_chart()` function provided by Streamlit. This function takes the Altair chart as its argument.

  3) **Display in Streamlit App:** When your Streamlit app runs and encounters the `st.altair_chart()` function with your Altair chart, it will render the chart directly within your Streamlit app. This allows your users to interact with and explore the Altair chart alongside other content in your app.

### **Plotly Charts**

Streamlit supports Plotly for interactive charts. You can display Plotly charts in your app using the `st.plotly_chart()` function.

### **Vega-Lite Charts**

You can create Vega-Lite charts with Streamlit using the `st.vega_lite_chart()` function. This function allows you to display Vega-Lite charts in your app.

### **Bokeh Charts**

Bokeh charts are also supported in Streamlit. You can display Bokeh charts in your app using the `st.bokeh_chart()` function.

### **Pydeck Charts**

Streamlit supports Pydeck for 3D visualizations. You can display Pydeck charts in your app using the st.`pydeck_chart()` function.

## Status elements

### **Spinner**

You can display a spinner to indicate that a task is in progress:

`st.spinner()`: Display a spinner animation.

### **Progress Bar**

Show the progress of a task with a progress bar:

`st.progress()`: Display a progress bar to visualize task completion.

### **Info, Success, Warning, Error Messages:**

Display informational messages or notifications using different styles:

`st.info()`: Display an informational message.
`st.success()`: Display a success message.
`st.warning()`: Display a warning message.
`st.error()`: Display an error message.

### **Empty Placeholder**

Create an empty placeholder for dynamic updates:

`st.empty()`: Create an empty placeholder for dynamic content updates.

### **Code Execution Time**

Measure and display the execution time of code blocks:

`st.code()` with `timeit`: Measure and display the execution time of code blocks using Python's `timeit` module.

## Download button

### **section** 
- "Download Button" Streamlit allows you to add a download button to enable users to download data or reports directly from your app.

### **subsection** 
"Basic Download Button" You can add a basic download button using the `st.download_button()` function:

- `st.download_button(label, data, file_name, mime=None, key=None, help=None)`: Display a download button with the specified label and data.

### **subsection** 
- "Example Usage" Here's an example of how to use the `st.download_button()` function to create a download button:

- **EXAMPLE**
```python
import streamlit as st

data_to_download = "Hello, world!"

if st.button("Download Data"):
    st.download_button(label="Download", data=data_to_download, file_name="data.txt", mime="text/plain")
```
- In this example, when the user clicks the "Download Data" button, a download button labeled "Download" will appear, allowing the user to download the data as a text file named "data.txt".

## First App in streamlit

**THIS IS source code LINK 👇**

[Github link](https://github.com/tamaraiselva/git-demo/tree/main/resume)


![image](images/p.png)

![image](images/g.png)

![image](images/f.png)

## Streamlit with SQL server using SQLite3L
- To integrate Streamlit with an SQL server using SQLite3 and present it using LiaScript, you'll need to follow these general steps:

 1) Set Up SQLite Database: Ensure you have SQLite3 installed. Create a SQLite database and populate it with your data.

 2) Write Streamlit App: Develop a Streamlit application in Python. Use the SQLite3 library to connect to your SQLite database, query data, and display it in your Streamlit app.

 3) Deploy Streamlit App: Host your Streamlit application. You can use Streamlit Sharing, Heroku, or any other platform that supports deploying Streamlit apps.

 4) Embed in LiaScript: In your LiaScript document, embed the hosted Streamlit app using an iframe.

Here's a basic example:

Assuming you have a Streamlit app named `app.py`:

``` python

import streamlit as st
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('your_database.db')
c = conn.cursor()

# Query data
c.execute('SELECT * FROM your_table')
data = c.fetchall()

# Display data using Streamlit
st.write(data)

# Close connection
conn.close()

```
And a LiaScript document:

``` python

# Streamlit App Embedded in LiaScript

<iframe src="https://your-streamlit-app-url.com" width="1000" height="600"></iframe>

```
- Replace 'your_database.db' with the path to your SQLite database and 'your_table' with the name of your table. Also, replace 'https://your-streamlit-app-url.com' with the URL where your Streamlit app is hosted.

- This way, when someone views your LiaScript document, they'll see the Streamlit app embedded in an iframe.

## Login page

- To create a login page using LiaScript, you can leverage the capabilities of HTML and CSS within LiaScript. Below is a simple example of how you can create a login page

```  python
# Login Page

<form>
  <div>
    <label for="username">Username:</label>
    <input type="text" id="username" name="username" placeholder="Enter your username">
  </div>
  <div>
    <label for="password">Password:</label>
    <input type="password" id="password" name="password" placeholder="Enter your password">
  </div>
  <div>
    <button type="submit">Login</button>
  </div>
</form>

<style>
  form {
    max-width: 300px;
    margin: 0 auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
  }
  div {
    margin-bottom: 10px;
  }
  label {
    display: block;
    font-weight: bold;
  }
  input[type="text"],
  input[type="password"] {
    width: 100%;
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 5px;
  }
  button {
    width: 100%;
    padding: 10px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  button:hover {
    background-color: #45a049;
  }
</style>

```
- This Markdown code will render a login form with fields for username and password. When the form is submitted, it will not perform any action since LiaScript doesn't support form submission. However, you can use JavaScript to handle form submission and perform authentication if needed.

## Deploy App to Streamlit Cloud
- As of my last update in January 2022, there's no direct integration between Streamlit Cloud and LiaScript. Streamlit Cloud is designed to deploy and share Streamlit apps, while LiaScript is a Markdown-based tool for creating interactive online courses. However, you can use LiaScript to create interactive tutorials or documentation for your Streamlit app and provide links to the deployed Streamlit app within the LiaScript document.

- Here's a general guide on how you can achieve this:

 1) **Create Streamlit App** Develop your Streamlit application in Python. Make sure it's working locally before proceeding.

 2) **Deploy Streamlit App** Host your Streamlit app on Streamlit Cloud. You can follow Streamlit's documentation on how to deploy your app to Streamlit Cloud.

 3) **Create LiaScript Document** Write your tutorial or documentation using LiaScript. Within the LiaScript document, you can provide explanations, code snippets, and instructions on how to use your Streamlit app.

 4) **Embed Streamlit App Link** In your LiaScript document, include a link to your deployed Streamlit app. You can use regular Markdown syntax for linking, like [Link to Streamlit App](https://streamlit.io/cloud).

 5) **Publish LiaScript Document** Once your LiaScript document is ready, you can publish it on a platform that supports LiaScript, such as GitHub Pages or your own website.

## Conclusion

Streamlit is a powerful tool for building interactive web applications with Python. With its intuitive interface and extensive functionality, you can quickly create data-driven apps that engage and inform your audience. Start building your own Streamlit apps today and unlock the full potential of your data

``` python 

This LIA script provides a structured guide covering all the topics mentioned in your Streamlit document, from installation to deployment. It offers explanations, code snippets, and instructions to help users understand and implement each aspect of building Streamlit applications.

```
## Reference

if to learn click this link button 👇

1) [Reference link](https://www.youtube.com/playlist?list=PLqcaZayCJLpKIelj955Iq62cqcL4vAlm7)

2) [Reference link](https://www.youtube.com/watch?v=VqgUkExPvLY)

3) [Reference link](https://www.youtube.com/watch?v=i6gt2OKezOQ&t=1s)