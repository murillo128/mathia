# MI-025 — Regular sampling separates exact phase aliasing from finite-window stability

**Evidence level:** supported by the exact phase-pushforward classification and remote-frequency recurrence in AF-279; restricted to the stated absolutely convergent Dirichlet-series source class.

For

\[
F(s)=\sum_n a_ne^{-\lambda_n s},\qquad \sum_n|a_n|e^{-c\lambda_n}<\infty,
\]

sampling only on the regular vertical lattice `c+ikh` does not retain the frequency coordinate `lambda_n` itself. It retains the pushed phase

\[
z_n=e^{-ih\lambda_n}.
\]

The complete bilateral sample sequence is exactly the Fourier--Stieltjes transform of

\[
\mu_F=\sum_n a_ne^{-c\lambda_n}\delta_{z_n}.
\]

Hence two sources have identical infinite lattice data iff their pushed measures agree. Exact coefficient recovery on a declared frequency system is therefore equivalent to injectivity of `lambda -> e^{-ih lambda}`.

For ordinary Dirichlet frequencies `lambda_n=log n`, put `q_h=e^{2\pi/h}`. Exact aliases occur precisely when `n/m=q_h^r` for some nonzero integer `r`; equivalently, full coefficient fidelity holds iff `q_h^r` is never a positive rational for nonzero `r`. Thus cadence is part of the quotient, not a neutral implementation detail.

Nonresonance does not solve finite acquisition. Fix an index `N` and a finite window `|k|<=K`. Choosing integers `m_j` nearest to `Nq_h^j` makes

\[
e^{-ih\log m_j}\to e^{-ih\log N},
\]

so opposite weighted coefficient perturbations at `N` and `m_j` have fixed weighted `\ell^1` size while their entire finite sample window tends to zero. The infinite map can be injective while every preassigned finite window has no uniform inverse modulus on the unrestricted weighted `\ell^1` ball.

The useful separation is therefore exact:

- **aliasing:** distinct source coordinates lie in the same phase fiber even with infinitely many lattice samples;
- **conditioning:** the phase map is injective, but remote coordinates approach the target phase so closely that a finite horizon cannot separate them uniformly.

Continuous vertical averaging in AF-278 pays unbounded time breadth without this phase quotient; regular sampling additionally pays cadence geometry. Any claim that discrete acquisition compresses the same information must price both losses separately.

**Boundary.** The classification uses bilateral samples and a known frequency system. One-sided sampling needs a separate uniqueness audit. A collision in the unrestricted Dirichlet class does not automatically construct a collision inside a narrower multiplicative Euler category, and the finite-window obstruction does not assert instability in every norm on the full infinite sample sequence.
