export default function EmploymentManagementSystem() {
  const cards = [
    { title: 'Employees', value: '1,248' },
    { title: 'Attendance', value: '96%' },
    { title: 'Leaves', value: '34 Pending' },
    { title: 'Payroll', value: '$84K' },
  ];

  const employees = [
    { name: 'John Carter', department: 'Engineering', status: 'Active' },
    { name: 'Emma Watson', department: 'HR', status: 'On Leave' },
    { name: 'David Miller', department: 'Finance', status: 'Active' },
    { name: 'Sophia Lee', department: 'Marketing', status: 'Pending Review' },
  ];

  return (
    <div className="min-h-screen bg-slate-100 flex">
      {/* Sidebar */}
      <aside className="w-72 bg-slate-900 text-white p-6 hidden md:flex flex-col justify-between">
        <div>
          <h1 className="text-3xl font-bold mb-10">EMS Dashboard</h1>

          <nav className="space-y-4 text-slate-300">
            {[
              'Dashboard',
              'Employees',
              'Attendance',
              'Leave Management',
              'Payroll',
              'Performance',
              'Notifications',
            ].map((item) => (
              <div
                key={item}
                className="hover:bg-slate-800 transition-all duration-300 p-3 rounded-xl cursor-pointer"
              >
                {item}
              </div>
            ))}
          </nav>
        </div>

        <button className="bg-blue-600 hover:bg-blue-700 transition-all p-3 rounded-xl font-semibold">
          Get in Touch
        </button>
      </aside>

      {/* Main Content */}
      <main className="flex-1 p-6 overflow-y-auto">
        {/* Header */}
        <div className="flex flex-col md:flex-row md:items-center md:justify-between mb-8 gap-4">
          <div>
            <h2 className="text-4xl font-bold text-slate-800">
              Employment Management System
            </h2>
            <p className="text-slate-500 mt-2">
              Modern HR & Employee Workflow Dashboard
            </p>
          </div>

          <button className="bg-slate-900 text-white px-6 py-3 rounded-2xl hover:scale-105 transition-all duration-300 shadow-lg">
            Add Employee
          </button>
        </div>

        {/* Metric Cards */}
        <div className="grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-4 gap-6 mb-8">
          {cards.map((card, index) => (
            <div
              key={card.title}
              className="bg-white rounded-3xl shadow-lg p-6 hover:-translate-y-2 transition-all duration-300"
              style={{ animationDelay: `${index * 120}ms` }}
            >
              <p className="text-slate-500 mb-2">{card.title}</p>
              <h3 className="text-4xl font-bold text-slate-800">
                {card.value}
              </h3>
            </div>
          ))}
        </div>

        {/* Charts & Analytics */}
        <div className="grid lg:grid-cols-2 gap-6 mb-8">
          <div className="bg-white rounded-3xl shadow-lg p-6">
            <div className="flex justify-between items-center mb-6">
              <h3 className="text-2xl font-bold text-slate-800">
                Headcount Trend
              </h3>
              <span className="text-green-600 font-semibold">+12%</span>
            </div>

            <div className="h-64 flex items-end gap-4">
              {[40, 60, 90, 70, 110, 130, 150].map((height, i) => (
                <div
                  key={i}
                  className="bg-blue-500 rounded-t-xl flex-1 hover:bg-blue-600 transition-all"
                  style={{ height: `${height}px` }}
                />
              ))}
            </div>
          </div>

          <div className="bg-white rounded-3xl shadow-lg p-6">
            <h3 className="text-2xl font-bold text-slate-800 mb-6">
              Department Distribution
            </h3>

            <div className="space-y-5">
              {[
                { dept: 'Engineering', width: '90%' },
                { dept: 'HR', width: '60%' },
                { dept: 'Finance', width: '50%' },
                { dept: 'Marketing', width: '70%' },
              ].map((item) => (
                <div key={item.dept}>
                  <div className="flex justify-between mb-2">
                    <span className="font-medium">{item.dept}</span>
                    <span>{item.width}</span>
                  </div>

                  <div className="w-full bg-slate-200 rounded-full h-4 overflow-hidden">
                    <div
                      className="bg-indigo-500 h-4 rounded-full transition-all duration-700"
                      style={{ width: item.width }}
                    />
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>

        {/* Employee Table */}
        <div className="bg-white rounded-3xl shadow-lg p-6 mb-8 overflow-hidden">
          <div className="flex items-center justify-between mb-6">
            <h3 className="text-2xl font-bold text-slate-800">
              Employee Management
            </h3>

            <input
              type="text"
              placeholder="Search employees..."
              className="border border-slate-300 rounded-xl px-4 py-2 w-64 focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
          </div>

          <div className="overflow-x-auto">
            <table className="w-full">
              <thead>
                <tr className="text-left border-b border-slate-200">
                  <th className="pb-4">Employee</th>
                  <th className="pb-4">Department</th>
                  <th className="pb-4">Status</th>
                  <th className="pb-4">Action</th>
                </tr>
              </thead>

              <tbody>
                {employees.map((employee) => (
                  <tr
                    key={employee.name}
                    className="border-b border-slate-100 hover:bg-slate-50 transition-all"
                  >
                    <td className="py-5 font-medium">{employee.name}</td>
                    <td>{employee.department}</td>
                    <td>
                      <span className="bg-green-100 text-green-700 px-3 py-1 rounded-full text-sm">
                        {employee.status}
                      </span>
                    </td>
                    <td>
                      <button className="bg-blue-600 text-white px-4 py-2 rounded-xl hover:bg-blue-700 transition-all">
                        View
                      </button>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>

        {/* Request Modal Preview */}
        <div className="bg-white rounded-3xl shadow-lg p-6 max-w-2xl">
          <h3 className="text-2xl font-bold text-slate-800 mb-6">
            Leave Request Form
          </h3>

          <div className="space-y-5">
            <input
              value="John Carter"
              readOnly
              className="w-full border border-slate-300 rounded-xl p-4 bg-slate-100"
            />

            <select className="w-full border border-slate-300 rounded-xl p-4">
              <option>Leave</option>
              <option>Query</option>
              <option>Document Request</option>
            </select>

            <input
              type="date"
              className="w-full border border-slate-300 rounded-xl p-4"
            />

            <textarea
              placeholder="Enter your reason or message"
              rows={5}
              className="w-full border border-slate-300 rounded-xl p-4"
            />

            <button className="bg-slate-900 text-white px-6 py-4 rounded-2xl hover:scale-105 transition-all duration-300">
              Submit Request
            </button>
          </div>
        </div>
      </main>
    </div>
  );
}
