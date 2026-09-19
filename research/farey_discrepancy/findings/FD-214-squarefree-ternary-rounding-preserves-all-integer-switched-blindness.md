# FD-214 — Squarefree ternary rounding preserves all-integer switched blindness

- **Date:** 2026-09-19
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** squarefree ternary realization / switched root-filter countermodel / probabilistic rounding / multiplicativity boundary
- **Depends on:** FD-213
- **Classification:** `EXACT-SQUAREFREE-SUPPORT + UNIT-SIGN-AMPLITUDE + PROBABILISTIC-EXISTENCE + ALL-INTEGER-CRITICAL-BLINDNESS + SUPER-SQRT-SUMMATORY-GROWTH + REPRESENTATION-BOUNDARY`

## Claim

`FD-213` shows that the dyadic-band schedule

\[
q(n)=q_j,\qquad j=\lfloor\log_2 n\rfloor,\qquad
q_j=
\begin{cases}
0,&j\equiv0\pmod3,\\
3,&j\equiv1,2\pmod3,
\end{cases}
\tag{1}
\]

admits a bounded real source whose selected root filter

\[
\mathcal C_q^A(n):=(T-I)^q[A(2n)-A(n)]=(T-I)^{q+1}A(n),
\qquad (TF)(n)=F(2n),
\tag{2}
\]

vanishes at every integer while its summatory function grows like \(N^\alpha\) with

\[
\alpha=\frac43\log_2\frac{1+\sqrt5}{2}
\approx0.9256558848>\frac12.
\tag{3}
\]

The open representation question was whether the exact squarefree support and unit amplitudes of the Möbius source already forbid that all-integer switched blind mode.

They do not. There exists a deterministic sequence \((\xi_n)_{n\ge1}\) obtained by fixing one outcome of an independent rounding scheme such that

\[
\boxed{\xi_n\in\{-1,0,1\},\qquad \xi_n^2=\mu(n)^2\quad(n\ge1),}
\tag{4}
\]

and, with

\[
X(N):=\sum_{n\le N}\xi_n,
\tag{5}
\]

one has simultaneously

\[
\boxed{
\mathcal C_{q(n)}^X(n)=O\!\left(\sqrt{n\log n}\right)
\qquad(n\ge2),
}
\tag{6}
\]

while along the explicit interior points

\[
N_m=3\,2^{3m-1}
\tag{7}
\]

from `FD-213`,

\[
\boxed{
|X(N_m)|\asymp N_m^\alpha.
}
\tag{8}
\]

Thus the switched observation satisfies the full RH-scale pointwise estimate

\[
\mathcal C_{q(n)}^X(n)=O_\varepsilon(n^{1/2+\varepsilon})
\tag{9}
\]

at **every integer**, yet the source summatory function violates the square-root exponent by the fixed amount \(\alpha-1/2\approx0.4256558848\).

This is still not a Möbius counterexample. Equation (4) gives the exact Möbius zero pattern and exact unit magnitude on every squarefree integer, but the signs are not multiplicatively compatible. The result therefore removes squarefree support and unit amplitudes as explanations for why the `FD-213` Floquet mode might fail physically; genuine Möbius sign correlation remains outside the construction.

## 1. Start from the profile-lifted blind mode

Use the concrete `FD-213` construction

\[
A(N)=\varepsilon\,a_{j(N)}h(t(N)),
\qquad
j(N)=\lfloor\log_2N\rfloor,
\qquad
t(N)=\frac{N}{2^{j(N)}},
\tag{10}
\]

with

\[
h(t)=(t-1)(2-t).
\tag{11}
\]

Its Floquet amplitudes satisfy

\[
|a_j|\ll \rho^j,
\qquad
\rho=\left(\frac{1+\sqrt5}{2}\right)^{4/3}
=2^\alpha<2,
\tag{12}
\]

and `FD-213` proves exactly that

\[
\mathcal C_{q(n)}^A(n)=0
\qquad(n\ge1),
\tag{13}
\]

together with

\[
|A(N_m)|\asymp N_m^\alpha.
\tag{14}
\]

Let

\[
v_n:=A(n)-A(n-1).
\tag{15}
\]

Because \(h\) is quadratic, the increment has one derivative of dyadic smoothing inside each band. Uniformly for \(2^j<n<2^{j+1}\),

\[
|v_n|\ll \varepsilon\,\rho^j2^{-j}\ll_\varepsilon n^{\alpha-1},
\tag{16}
\]

and away from a dyadic boundary,

\[
|v_{n+1}-v_n|
\ll \varepsilon\,\rho^j2^{-2j}
\ll_\varepsilon n^{\alpha-2}.
\tag{17}
\]

At a boundary \(n=2^j\), the endpoint identities \(h(1)=h(2)=0\) give the weaker but still sufficient jump estimate

\[
|v_{n+1}-v_n|\ll_\varepsilon n^{\alpha-1}.
\tag{18}
\]

There is only one such jump per dyadic band. Since \(\alpha<1\), shrinking \(\varepsilon\) if necessary makes the increments arbitrarily small without changing (13) or the exponent in (14).

## 2. Project the real source onto exact squarefree support

Put

\[
\delta:=\frac1{\zeta(2)}=\frac6{\pi^2}.
\tag{19}
\]

Choose the scale \(\varepsilon\) in (10) small enough that

\[
|v_n|\le\delta
\qquad(n\ge1).
\tag{20}
\]

Define the squarefree-supported fractional source

\[
b_n:=\delta^{-1}\mu(n)^2v_n,
\qquad
B(N):=\sum_{n\le N}b_n.
\tag{21}
\]

Then \(b_n=0\) off the squarefrees and \(|b_n|\le1\) everywhere.

The loss from imposing the squarefree zero pattern is much smaller than the blind profile itself. The elementary identity

\[
\mu(n)^2=\sum_{d^2\mid n}\mu(d)
\tag{22}
\]

gives, without any zero-free input,

\[
Q(x):=\sum_{n\le x}\mu(n)^2
=\delta x+O(\sqrt x).
\tag{23}
\]

Indeed,

\[
Q(x)
=
\sum_{d\le\sqrt x}\mu(d)\left\lfloor\frac{x}{d^2}\right\rfloor
=
x\sum_{d\le\sqrt x}\frac{\mu(d)}{d^2}+O(\sqrt x)
=
\frac{x}{\zeta(2)}+O(\sqrt x).
\tag{24}
\]

Write

\[
R(x):=Q(x)-\delta x=O(\sqrt x).
\tag{25}
\]

Then

\[
B(N)-A(N)
=
\delta^{-1}\sum_{n\le N}\bigl(\mu(n)^2-\delta\bigr)v_n.
\tag{26}
\]

Discrete summation by parts gives

\[
\sum_{n\le N}\bigl(\mu(n)^2-\delta\bigr)v_n
=
R(N)v_N+
\sum_{n<N}R(n)(v_n-v_{n+1}).
\tag{27}
\]

On a dyadic band of size \(2^j\), equations (17) and (25) make the interior contribution

\[
O\!\left(
2^j\cdot 2^{j/2}\cdot2^{j(\alpha-2)}
\right)
=
O\!\left(2^{j(\alpha-1/2)}\right).
\tag{28}
\]

The single boundary jump (18) in that band contributes the same order,

\[
O\!\left(
2^{j/2}\cdot2^{j(\alpha-1)}
\right)
=
O\!\left(2^{j(\alpha-1/2)}\right).
\tag{29}
\]

Because \(\alpha>1/2\), the dyadic sum is dominated by its last band. Together with the endpoint term in (27),

\[
\boxed{
B(N)=A(N)+O\!\left(N^{\alpha-1/2}\right).
}
\tag{30}
\]

In particular the squarefree projection retains the super-square-root profile because

\[
\alpha-\frac12<\alpha.
\tag{31}
\]

Its switched residual is also subcritical relative to the square-root scale. Since the filter orders in (1) are bounded by four applications of \(T-I\), (13) and (30) imply

\[
\mathcal C_{q(n)}^B(n)
=
O\!\left(n^{\alpha-1/2}\right)
=
o(\sqrt n),
\tag{32}
\]

where the final relation uses the equally essential inequality \(\alpha<1\).

Thus exact squarefree support alone already leaves the all-integer blind mechanism intact.

## 3. Round every squarefree amplitude to an exact sign

It remains to replace the fractional squarefree amplitudes \(b_n\in[-1,1]\) by exact unit signs without losing the pointwise switched estimate.

For every squarefree \(n\), independently choose

\[
\xi_n=
\begin{cases}
+1,&\text{with probability }(1+b_n)/2,\\
-1,&\text{with probability }(1-b_n)/2,
\end{cases}
\tag{33}
\]

and put \(\xi_n=0\) when \(n\) is not squarefree. If desired, \(\xi_1=1\) can be fixed deterministically; this changes only a constant summatory offset and is killed by every filter in (2).

Then

\[
\mathbb E\xi_n=b_n,
\qquad
\xi_n^2=\mu(n)^2
\tag{34}
\]

exactly. Define

\[
Z_n:=\xi_n-b_n,
\qquad
W(N):=\sum_{n\le N}Z_n.
\tag{35}
\]

The \(Z_n\) are independent, centered and uniformly bounded. The elementary exponential-moment estimate for bounded centered independent variables therefore gives an absolute \(c>0\) such that

\[
\Pr\!\left(|W(N)|>C\sqrt{N\log N}\right)
\le
2N^{-cC^2}.
\tag{36}
\]

Choose \(C\) so that the right side is summable in \(N\). Borel--Cantelli then shows that with probability one,

\[
W(N)=O\!\left(\sqrt{N\log N}\right)
\qquad\text{for all }N.
\tag{37}
\]

Fix one realization with this property. This turns the probabilistic construction into one deterministic source satisfying (4).

For that realization,

\[
X(N)=B(N)+W(N)
=
A(N)
+
O\!\left(N^{\alpha-1/2}\right)
+
O\!\left(\sqrt{N\log N}\right).
\tag{38}
\]

Since \(\alpha>1/2\), both errors are \(o(N^\alpha)\). Evaluating at the explicit points (7) and using (14) proves (8).

For the switched filter, write \(r(n)=q(n)+1\in\{1,4\}\). Every \((T-I)^{r(n)}\) uses only finitely many values \(F(2^kn)\), with \(0\le k\le4\), and its binomial coefficient mass is uniformly bounded. Hence (32) and (37) yield

\[
\begin{aligned}
\mathcal C_{q(n)}^X(n)
&=
\mathcal C_{q(n)}^B(n)
+
(T-I)^{r(n)}W(n)\\
&=
O\!\left(n^{\alpha-1/2}\right)
+
O\!\left(\sqrt{n\log n}\right)\\
&=
O\!\left(\sqrt{n\log n}\right),
\end{aligned}
\tag{39}
\]

because \(\alpha<1\). This proves (6).

## 4. What this closes, and what it does not

`FD-213` left two conspicuous source-specific features absent from its bounded-source countermodel: the Möbius squarefree zero pattern and multiplicative sign compatibility. The present construction separates them.

The squarefree pattern is not enough. More strongly, even the exact pointwise amplitude law

\[
|\xi_n|=\mu(n)^2
\tag{40}
\]

is not enough. One can impose zero on every nonsquarefree integer, force a unit sign on every squarefree integer, retain super-square-root summatory growth, and still keep the selected all-integer switched root filter inside the RH-scale pointwise envelope.

What is missing is not a small local correction. For the physical Möbius source, squarefree signs obey the global law

\[
\mu(ab)=\mu(a)\mu(b)
\qquad((a,b)=1),
\tag{41}
\]

with every prime assigned sign \(-1\). The independent rounding in (33) deliberately violates this correlation. `FD-214` therefore does **not** show that Möbius can realize the blind profile, nor does it refute a scale-varying Farey criterion specialized to Möbius. It shows that any proof which kills the `FD-213` mechanism must use more than support and magnitude information; multiplicative sign compatibility, a comparably strong exact arithmetic relation, or a genuinely mantissa-mixing observation remains necessary.

This also explains why the construction is not a restatement of the earlier squarefree-sign controls `FD-007--008`. Those findings show that exact squarefree ternary sources can saturate a fixed-horizon GCD-energy relaxation, even after one divisor identity is imposed. Here the target is different: one coherent infinite source is required to satisfy an all-integer, scale-varying switched root-filter estimate while retaining supercritical summatory growth. The profile projection plus global rounding establishes that stronger coherence statement for the present dilation mechanism.

## 5. Prior-art and novelty boundary

No new analytic number-theory theorem is imported. The squarefree density estimate (23) is derived directly from (22), and the rounding step uses only the standard probabilistic-method fact that independent bounded mean-zero partial sums have exponentially decaying \(\sqrt{N\log N}\)-scale tails. The latter estimate is reproduced in the exact strength needed in (36)--(37).

Randomized rounding and concentration of independent bounded variables are classical, and no novelty is claimed for them. A prior-art search found no direct treatment of the present combination: projection of a switched dyadic Floquet null profile to exact squarefree support, followed by unit-sign rounding while preserving an all-integer critical root-filter bound. No new durable `SOURCES.md` anchor is required because all number-theoretic input used in the proof is elementary and the probabilistic step is self-contained at the stated level.

The novel claim is restricted to the representation boundary (4), (6), and (8): the `FD-213` switched blind mode survives the exact squarefree ternary alphabet.

## 6. Falsification and audit boundary

The proof depends on four quantitative inequalities that should remain explicit.

First, the `FD-213` exponent satisfies

\[
\frac12<\alpha<1.
\tag{42}
\]

The lower inequality makes the profile dominate the rounding noise in (38); the upper inequality makes the squarefree-projection error in (32) strictly smaller than \(\sqrt n\).

Second, the summation-by-parts estimate must include dyadic boundary jumps. Ignoring them would incorrectly treat \(v_n\) as globally \(C^1\)-smooth. Equation (18) shows that each boundary contributes exactly the same \(N^{\alpha-1/2}\) scale as a whole band of interior second differences, and there are only logarithmically many geometrically increasing contributions.

Third, the rounding is performed on the **source increments**, not on summatory values. Therefore (4) is exact after fixing one realization. The price is the unavoidable \(O(\sqrt{N\log N})\) partial-sum discrepancy, which is still small enough because \(\alpha>1/2\).

Fourth, the construction preserves only support and magnitude. It does not preserve Möbius multiplicativity, the fixed prime sign pattern, or the full family of divisor identities that those properties imply. Any downstream use must keep that representation boundary intact.

Within those boundaries, the conclusion is deterministic: at least one exact squarefree ternary source satisfies (4), (6), and (8). Squarefree support plus unit amplitudes therefore cannot by themselves eliminate the all-integer switched Floquet obstruction.
