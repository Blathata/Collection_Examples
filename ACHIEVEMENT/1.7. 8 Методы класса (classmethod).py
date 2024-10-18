yu_a_makarin = Spaceman(
    name='Юрий Алексеевич Макарин',
    space_experience=10,
    father=Spaceman(
        name='Алексей Михайлович Макарин',
        space_experience=25,
        mother=Spaceman(
            name='Евгения Владимировна Беляева',
            space_experience=1
        )
    ),
    mother=Spaceman('Ангелина Васильевна Черенкова', 5)
)

print(yu_a_makarin)