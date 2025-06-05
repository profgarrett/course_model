---
title: "ROI Rmd Sample"
author: "Nathan Garrett"
date: "2024-07-18"
output: html_document
---

```{r setup, include=FALSE}
knitr::opts_chunk$set(echo = TRUE)

# Key [Syntax](https://rmarkdown.rstudio.com/lesson-8.html)

```

# CarMax ROI Problem

![Honda CRX](https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/Honda_CR-X_1987.jpg/560px-Honda_CR-X_1987.jpg)

## Thesis: 

The total cost of ownership for buying a new Honda CRX is lower than buying a 2-year old car from CarMax. 
The new car was *$40,242*, and the two-year car was *$33,370*. 

The difference is the result of the older car being 2/3rds the initial purchase cost. The older car's higher maintenance balances the higher interest of the newer car.

``` {r}
source('http://biostatmatt.com/R/amortize.R')

downpayment <- 5000
apr <- 10
years <- 6

model <- 'Rav4'
old_cost <- 21998 # 2016, 69k miles
old_financing <- (old_cost - downpayment)
old_maintenance <- 7600 * 0.75
old_monthly_payment <- payment(old_financing, apr, 12*years)
old_amortization_table <- amortize(old_financing, old_monthly_payment, apr, 12*years)
old_total_interest <- max(old_amortization_table$interest)

old_tco <- old_cost + old_total_interest + old_maintenance

new_cost <- 30000
new_financing <- new_cost - downpayment
new_maintenance <- 7600 * 0.25
new_monthly_payment <- payment(new_financing, apr, 12*years)
new_amortization_table <- amortize(new_financing, new_monthly_payment, apr, 12*years)
new_total_interest <- max(new_amortization_table$interest)

new_tco <- new_cost + new_total_interest + new_maintenance

barplot(c(new_tco, old_tco), 
        names.arg = c('New Car TCO', 'Old Car TCO'))
```

## Method

Total cost of ownership included the following variables:

- Initial car purchase price
- Financing cost ($5,000 downpayment, 10% APR)
- Estimated annual maintenance 

## Limitations

Purchase cost was pulled from Carmax and dealer websites. Annual maintenance estimated from personal experience.