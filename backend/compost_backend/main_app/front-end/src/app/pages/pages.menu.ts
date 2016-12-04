export const PAGES_MENU = [
  {
    path: 'pages',
    children: [
      {
        path: 'dashboard',
        data: {
          menu: {
            title: 'Dashboard',
            icon: 'ion-android-home',
            selected: false,
            expanded: false,
            order: 0
          }
        }
      },

      {
        path: '',
        data: {
          menu: {
            title: 'Admin',
            icon: 'ion-document',
            selected: false,
            expanded: false,
            order: 650,
          }
        },
        children: [
          {
            path: ['/login'],
            data: {
              menu: {
                title: 'Login'
              }
            }
          },
          {
            path: ['/register'],
            data: {
              menu: {
                title: 'Register'
              }
            }
          }
        ]
      },

      {
        path: '',
        data: {
          menu: {
            title: 'Learn More',
            url: 'http://www.oregonmetro.gov/tools-living/yard-and-garden/composting',
            icon: 'ion-android-exit',
            order: 800,
            target: '_blank'
          }
        }
      }
    ]
  }
];
