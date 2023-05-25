## Introduction

For the final project, you will conduct your own data analysis within a Jupyter notebook and use it to create a sharable file that documents your findings. You should start by taking a look at your dataset and brainstorming what questions you could answer using it. Then you should use pandas and NumPy to answer the questions you are most interested in, and create a report sharing the answers. You will not be required to use inferential statistics or machine learning to complete this project, but you should make it clear in your communications that your findings are tentative. This project is open-ended in that we are not looking for one right answer.

### Step One - Choose Your Data Set

<div class="markdown_table-responsive__Bf7V6"><table class="markdown_table__luvPz markdown_table-striped__8FWX9">
<thead>
<tr>
<th>Data Set</th>
<th>Overview and Notes</th>
<th>Example Questions</th>
</tr>
</thead>
<tbody>
<tr>
<td>TMDb movie data - (cleaned from original data on <a target="_blank" href="https://www.kaggle.com/tmdb/tmdb-movie-metadata">Kaggle</a>)</td>
<td>This data set contains information about 10,000 movies collected from The Movie Database (TMDb), including user ratings and revenue.  <ul> <li>Certain columns, like ‘cast’ and ‘genres’, contain multiple values separated by pipe (|) characters.</li> <li>There are some odd characters in the ‘cast’ column. Don’t worry about cleaning them. You can leave them as is.</li> <li>The final two columns ending with “_adj” show the budget and revenue of the associated movie in terms of 2010 dollars, accounting for inflation over time.</li> </ul></td>
<td>Which genres are most popular from year to year? What kinds of properties are associated with movies that have high revenues?</td>
</tr>
<tr>
<td>No-show appointments - (original source on <a target="_blank" href="https://www.kaggle.com/datasets/joniarroba/noshowappointments">Kaggle</a>)</td>
<td>This dataset collects information from 100k medical appointments in Brazil and is focused on the question of whether or not patients show up for their appointment. A number of characteristics about the patient are included in each row.  <ul> <li>‘ScheduledDay’ tells us on what day the patient set up their appointment.</li> <li>‘Neighborhood’ indicates the location of the hospital.</li> <li>‘Scholarship’ indicates whether or not the patient is enrolled in Brasilian welfare program <a target="_blank" href="https://en.wikipedia.org/wiki/Bolsa_Fam%C3%ADlia">Bolsa Família</a>.</li> <li>Be careful about the encoding of the last column: it says ‘No’ if the patient showed up to their appointment, and ‘Yes’ if they did not show up.</li> </ul></td>
<td>What factors are important for us to know in order to predict if a patient will show up for their scheduled appointment?</td>
</tr>
<tr>
<td>FBI Gun Data - (original source on <a target="_blank" href="https://github.com/BuzzFeedNews/nics-firearm-background-checks/blob/master/README.md">Github</a>)</td>
<td>The data comes from the FBI's National Instant Criminal Background Check System. The NICS is used by to determine whether a prospective buyer is eligible to buy firearms or explosives.  
Gun shops call into this system to ensure that each customer does not have a criminal record or isn’t otherwise ineligible to make a purchase.  
The data has been supplemented with state level data from <a target="_blank" href="https://www.census.gov/">census.gov</a>.  <ul> <li>The <a target="_blank" href="https://docs.google.com/viewer?url=https%3A%2F%2Fd17h27t6h515a5.cloudfront.net%2Ftopher%2F2017%2FNovember%2F5a0a4db8_gun-data%2Fgun-data.xlsx">NICS data</a> is found in one sheet of an .xlsx file. It contains the number of firearm checks by month, state, and type.</li> <li>The <a target="_blank" href="https://d17h27t6h515a5.cloudfront.net/topher/2017/November/5a0a554c_u.s.-census-data/u.s.-census-data.csv">U.S. census data</a> is found in a .csv file. It contains several variables at the state level. Most variables just have one data point per state (2016), but a few have data for more than one year.</li> </ul></td>
<td>What census data is most associated with high gun per capita? Which states have had the highest growth in gun registrations? What is the overall trend of gun purchases?</td>
</tr>
</tbody>
</table>
</div>

You **must** choose one of these datasets to complete the project.
All datasets are provided for you within the project workspace.

### Step Two - Get Organized

Eventually you’ll want to submit your project (and share it with friends, family, and employers). Since we are using a Jupyter notebook, you'll be able to submit both the code you wrote and the report of your findings in the same document.

It is recommended that you use the workspace provided in *Project Workspace: Complete and Submit Project*, where you can do all your work and submit the project directly.

If your are using the workspace provided for the project, you are in luck! The workspace is already organized for you. There you will find the Jupyter notebook for your analysis and report, as well as the three datasets for you to choose from.

If you decide to work locally, get organized before you begin. We recommend creating a single folder that will eventually contain:

* The **Jupyter notebook** you wrote as part of your analysis and report
* The **data set** you used (which you will not need to submit)

You can download the **notebook template** and **dataset** of your choosing from the project workspace. It is a great starting point to help organize your investigation.

### Step Three - Analyze Your Data

Brainstorm some questions you could answer using the data set you chose, then start answering those questions. You can find some questions in the data set options table above to help you get started.

Try and suggest questions that promote looking at relationships between multiple variables. You should aim to analyze at least one dependent variable and three independent variables in your investigation. Make sure you use NumPy and pandas where they are appropriate!

### Step Four - Share Your Findings

Once you have finished analyzing the data, create a report that shares the findings you found most interesting. Make sure that your report text is contained in Markdown cells to clearly distinguish your comments and findings from your code work. Feel free to use other tools and software to craft your final report, but make sure that you can submit your report as an HTML or PDF file so that it can be opened easily.

### Step Five - Review

Use the <a href="https://review.udacity.com/#!/rubrics/3298/view" target="_blank">**Project Rubric**</a> to review your project. If you are happy with your submission, then you're ready to submit your project. If you see room for improvement, keep working to improve your project!