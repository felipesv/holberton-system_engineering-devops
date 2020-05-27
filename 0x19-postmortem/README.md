## Incident summary
At 8:00 p.m. on Friday, July 26, 2019, half of the waiters and some customers of a restaurant noticed the increase in the values of the taxes charged to the customer at the time of passing the respective collection accounts.

This event is triggered when the changes of “New product tax percentage” were uploaded at 7:00 pm the same day.

This change contained the new calculation of the tax percentages for each dish or service consumed by the customer. This change was given in order to comply with the law imposed by the government, which implied changing the data of the percentages of each dish and service in the database, as well as the formula with which the total values of the invoice were calculated that was delivered to the customer.

The bug that appeared in the system was in the formula that was in charge of making the respective calculations based on the order or services used by the client, since it took values from a table where were kept the exact percentage values of tax for each one of the dishes and services  per the year, and the values did not correspond for the real values. These provided alterations since they were not the official ones but rather tests made by the development team with fictitious values, which indicates that at the time of making the changes in the production server some values in test environments were switched to production or passes to production.

## Detection

The development team received the problem at 8:15 pm the same day, and the error was found quickly, since there are tables with process events that happen every time the invoices are made, which together with the incident reports sent by the users (waiters) could filter this information in the events table, which allowed finding the fault in the calculations that were taking place, reflecting that the values they used in those calculations were not correct. This detection occurred at 20:30 and correction was mounted on the servers again at 20:45.

## Impact

During the 45 minutes that the incident lasted, around 25 reports were sended by the restaurant's clients, where several of them generated delays in their times, having to wait for them to generate invoices with their real values manually, thus In this way, many of the waiters stopped serving various tables that they were in charge of and customers that were arriving as they had to carry out these accounts to be able to dispatch those that were already in the restaurant. In general, there were delays in customer service, there was a loss of customers since they could not be served, which represented monetary losses for the restaurant.

## Response

Within the development team there were several team participants who were involved in the production deployment part who were given responsibility for the failure that occurred. These same characters were in charge of creating new protocols for production deployments and who solved the event presented. It should be noted that the development team created new ways to counter this type of event by mounting a server with a previous version that can be used in the event of event types such as the one presented.

## Timeline

- 19:45:00 - Changes uploaded to the production server.
- 20:00:00 - First error detected.
- 20:15:00 - First billing failure report arrives.
- 20:20:00 - the team begins to search the matches of the events table together with the report sent.
- 20:30:00 - they find the problem
- 20:32:00 - The respective tables of the fault change
- 20:35:00 - Changes are mounted on the test server
- 20:37:00 - They carry out billing tests with real values
- 20:45:00 - Upload change to the production server
