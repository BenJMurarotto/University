def analyse_sightings(sightings):
    if len(sightings) > 0:
        print(f'Maximum sighted in one day: {(max(sightings))}')
        print(f'Minimum sighted in one day: {(min(sightings))}')
        print(f'Average sighted for all days: {(sum(sightings)/len(sightings))}')
    else:
        print('No data to analyse')


lions = []  # no lion sightings
dingoes = [1, 2, 3, 4, 5, 6, 7]
kangaroos = [10, 5, 3, 7, 5]
analyse_sightings(lions)
analyse_sightings(dingoes)
analyse_sightings(kangaroos)