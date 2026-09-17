# PC-337 — finite-point Mellin selectors collapse to the von Mangoldt endpoint

**Status:** `EXACT-DERIVED` + `DECISIVE-NEGATIVE` for the finite point-supported distributional Mellin continuation left open by PC-335 and PC-336.

PC-179 gives the exact signed cyclotomic radial-flux Mellin transform

\[
\mathcal R_n(s)
=-\Gamma(s)\zeta(s)A_n(s),
\qquad
A_n(s):=n^{1-s}\prod_{p\mid n}(1-p^{s-1}),
\tag{1}
\]

for `n>1` on every Mellin line `Re(s)=sigma>0`, with the removable endpoint value

\[
\mathcal R_n(1)=\Lambda(n).
\tag{2}
\]

PC-335 rules out bounded shell-independent Mellin multipliers as exact semiprime-null selectors. PC-336 then classifies distributions supported only at the distinguished endpoint `s=1` as generalized-von-Mangoldt jets, but it deliberately leaves point-supported singular symbols away from that endpoint open.

That remaining finite-point class can be closed exactly. Let `T` be any distribution of finite support on one fixed Mellin-frequency line

\[
s=\sigma+it,\qquad \sigma>0.
\tag{3}
\]

Equivalently, by the classical point-support structure theorem,

\[
T=\sum_{j=1}^J\sum_{k=0}^{K_j}a_{j,k}\,\delta_{t_j}^{(k)}.
\tag{4}
\]

Define its shell response

\[
L_T(n):=\langle T,\mathcal R_n(\sigma+it)\rangle.
\tag{5}
\]

Then the exact classification is

\[
\boxed{
L_T(pq)=0\quad\text{for every pair of distinct primes }p,q
}
\tag{6}
\]

implies

\[
\boxed{
\begin{array}{ll}
\sigma\neq1:&L_T(n)=0\quad\text{for every }n>1,\\[1mm]
\sigma=1:&L_T(n)=c\,\Lambda(n)\quad\text{for every }n>1
\end{array}}
\tag{7}
\]

for one constant `c` depending on `T`.

Thus a finite collection of singular Mellin frequencies cannot build a new exact prime-power selector. **Modulo components invisible to the entire cyclotomic shell family, the only nonzero finite-point response annihilating every mixed-prime semiprime is the already-known endpoint evaluation `R_n(1)=Lambda(n)`.**

## 1. The radical factor turns mixed-prime controls into exponential polynomials

For a prime `p`, equation (1) gives

\[
A_p(s)=p^{1-s}-1,
\tag{8}
\]

and for distinct primes `p,q`,

\[
\boxed{A_{pq}(s)=A_p(s)A_q(s).}
\tag{9}
\]

More generally, introduce a continuous logarithmic scale parameter `x` by

\[
g_x(s):=e^{(1-s)x}-1.
\tag{10}
\]

Then `g_{log q}=A_q`. Fix a prime `p` and form the virtual mixed-prime response

\[
F_p(x):=\left\langle T,
-\Gamma(s)\zeta(s)A_p(s)g_x(s)
\right\rangle.
\tag{11}
\]

When `x=log q` with `q!=p` prime, this is exactly

\[
F_p(\log q)=L_T(pq)=0.
\tag{12}
\]

The important point is that `F_p(x)` is an exponential polynomial in the complex variable `x`.

First separate a possible endpoint component. Write

\[
T=T_0+T_*,
\tag{13}
\]

where `T_0` is supported at `t=0` when `sigma=1`, and is zero otherwise; `T_*` contains every other support point. Put

\[
U(s):=-\Gamma(s)\zeta(s).
\tag{14}
\]

`U` is smooth on the support of `T_*`, so multiplication of distributions defines another finite point-supported distribution

\[
S:=U\,T_*,
\qquad
\langle S,f\rangle:=\langle T_*,Uf\rangle.
\tag{15}
\]

At a nonendpoint support point

\[
s_j=\sigma+it_j,
\qquad
\lambda_j:=1-s_j\neq0,
\tag{16}
\]

each derivative in `t` falling on `e^{(1-s)x}` contributes a factor proportional to `x`. Hence the contribution of that support point to (11) has the form

\[
P_{j,p}(x)e^{\lambda_jx}+C_{j,p},
\tag{17}
\]

where `P_{j,p}` is a polynomial of degree at most the order of `S` at `t_j`.

The endpoint is also harmless. With `z=s-1` and

\[
G(z):=z\Gamma(1+z)\zeta(1+z),
\qquad G(0)=1,
\tag{18}
\]

one has

\[
-\Gamma(1+z)\zeta(1+z)
A_p(1+z)g_x(1+z)
=
-\frac{G(z)}{z}
(e^{-z\log p}-1)(e^{-zx}-1).
\tag{19}
\]

The two factors in parentheses each vanish once at `z=0`, so (19) is analytic there. Every finite endpoint jet is therefore an ordinary polynomial in `x`.

After consolidating equal support points, (11) has the canonical form

\[
\boxed{
F_p(x)=P_{0,p}(x)+
\sum_{j=1}^{J_*}P_{j,p}(x)e^{\lambda_jx},
}
\tag{20}
\]

with distinct nonzero `lambda_j`. This is the only structural input needed from the singular Mellin readout.

## 2. Prime logarithms are too dense to be zeros of a nonzero finite exponential polynomial

For completeness, the zero-density step can be derived directly rather than imported as a black box. Any nonzero function of the form (20) satisfies

\[
|F_p(z)|\le C(1+|z|)^K e^{\tau|z|}
\tag{21}
\]

for suitable constants `C,K,tau`. Choose `z_0` with `F_p(z_0)!=0` and apply Jensen's formula to `F_p(z_0+z)`. The growth bound (21) gives

\[
N_p(R)=O(R),
\tag{22}
\]

where `N_p(R)` counts zeros in a disk of radius `R`, with multiplicity.

But (12) supplies one distinct positive real zero at `log q` for every prime `q!=p`. Chebyshev's classical lower bound

\[
\pi(X)\gg \frac{X}{\log X}
\tag{23}
\]

therefore gives, for large `R`,

\[
\#\{q:\log q\le R/2\}
=\pi(e^{R/2})+O(1)
\gg \frac{e^{R/2}}{R},
\tag{24}
\]

which is incompatible with (22). Consequently

\[
\boxed{F_p\equiv0\quad\text{for every prime }p.}
\tag{25}
\]

This is much stronger than merely having infinitely many semiprime controls: the exponential-polynomial class has only linear zero density, whereas the logarithms of the primes have exponentially growing counting density in the `x` coordinate.

## 3. Every nonendpoint support component is shell-invisible

The generalized exponentials

\[
P(x)e^{\lambda x}
\tag{26}
\]

with distinct `lambda` are linearly independent. Hence (25) forces every nonzero-exponent polynomial `P_{j,p}` in (20) to vanish identically.

Fix one nonendpoint support point `s_j`, and let `K` be the maximal order with nonzero coefficient in the local effective distribution `S_j`. The coefficient of

\[
x^K e^{(1-s_j)x}
\tag{27}
\]

in `P_{j,p}(x)e^{(1-s_j)x}` is a nonzero universal scalar times

\[
a_{j,K}^{\mathrm{eff}}A_p(s_j).
\tag{28}
\]

For every `s_j!=1` there exists a prime `p` with `A_p(s_j)!=0`. In fact `p=2` or `p=3` already suffices: if both vanished, then with `beta=1-s_j`,

\[
e^{\beta\log2}=e^{\beta\log3}=1.
\tag{29}
\]

For `beta!=0` this would make `log2/log3` rational and hence imply a relation `2^m=3^n` with nonzero integers `m,n`, impossible. Thus simultaneous vanishing for `2` and `3` forces `beta=0`, i.e. `s_j=1`, contrary to the nonendpoint assumption.

Choose such a `p`. Equation (25) and (28) force the top coefficient of `S_j` to vanish. Descending in derivative order gives

\[
S_j=0.
\tag{30}
\]

Doing this at every nonendpoint support point yields

\[
\boxed{S=U T_*=0.}
\tag{31}
\]

The original distribution `T_*` need not itself be zero. For example, multiplication by the universal zeta envelope can annihilate special components supported at zeros of `zeta`. What matters is stronger for the present architecture: from (15) and (31),

\[
\boxed{
\langle T_*,\mathcal R_n\rangle
=\langle S,A_n\rangle=0
\quad\text{for every }n>1.
}
\tag{32}
\]

So every surviving nonendpoint component is invisible to the entire prime-circle radial shell family, not merely to semiprimes.

If `sigma!=1`, there is no endpoint component at all, and (32) proves the first case of (7).

## 4. On the endpoint line, the semiprime-null sector is one-dimensional

It remains to classify `T_0` when `sigma=1`. PC-336 gives the exact triangular equivalence

\[
\mathcal R_n^{(j)}(1)
=\frac{(-1)^j}{j+1}\Lambda_{j+1}(n)
+\text{a universal linear combination of }
\Lambda_1(n),\ldots,\Lambda_j(n),
\tag{33}
\]

where

\[
\Lambda_r(n)
:=\sum_{d\mid n}\mu(n/d)(\log d)^r.
\tag{34}
\]

Therefore every finite endpoint distribution has a shell response

\[
L_{T_0}(n)=\sum_{r=1}^{K+1}b_r\Lambda_r(n)
\tag{35}
\]

for suitable constants `b_r`, and conversely every such finite combination is realized by an endpoint jet.

For `n=pq` with distinct primes, put `u=log p` and `v=log q`. Then

\[
\Lambda_r(pq)
=(u+v)^r-u^r-v^r.
\tag{36}
\]

In particular `Lambda_1(pq)=0`. Suppose (35) vanishes for all distinct-prime semiprimes and let `R>=2` be the largest index with `b_R!=0`. Fix `p` and vary `q`. The expression

\[
\sum_{r=2}^{R}b_r\bigl((u+v)^r-u^r-v^r\bigr)
\tag{37}
\]

is an ordinary polynomial in `v` that vanishes at the infinitely many values `v=log q`. Its degree is `R-1`, and its leading coefficient is

\[
R\,u\,b_R\neq0,
\tag{38}
\]

a contradiction. Descending in `R` leaves only `b_1`.

Hence

\[
\boxed{
L_{T_0}(n)=b_1\Lambda(n),
}
\tag{39}
\]

which proves the second case of (7).

The common-vertex von Mangoldt evaluation is therefore not merely one example among many finite singular readouts. It spans the entire nontrivial semiprime-null response space within this finite point-supported Mellin class.

## 5. Prior-art and novelty audit

Every general analytic ingredient above is classical. Distributions supported at finitely many points are finite sums of delta derivatives; PC-336 already audits this through the Schwartz/Hormander point-support theorem. Generalized von Mangoldt functions and their almost-prime support are classical sieve-theoretic objects, also audited in PC-336.

The functions in (20) are classical exponential polynomials. A directed literature check found the expected century-old zero-distribution theory rather than a new spectral mechanism; a modern survey is J. Heittokangas, K. Ishizaki, K. Tohge and Z.-T. Wen, **Value distribution of exponential polynomials and their role in the theories of complex differential equations and oscillation theory**, *Bulletin of the London Mathematical Society* 55 (2023), DOI `10.1112/blms.12719`. The proof here does not require a specialized external zero theorem: the needed `O(R)` bound follows directly from Jensen plus (21), and the contradiction uses only the classical Chebyshev prime-counting lower bound.

Targeted searches around finite-support Mellin distributions, exponential-polynomial zeros at prime logarithms, and exact semiprime/prime-power selectors found no independent RH mechanism matching (7). No historical novelty is claimed for point-support theory, Jensen theory, prime-density estimates, or generalized von Mangoldt functions. The line-local contribution is the exact combination forced by the prime-circle radical factor: **finite singular Mellin frequencies either disappear from all shell responses or collapse to the original common-vertex `Lambda` channel.**

This is not a disguised recovery of `-zeta'/zeta` and does not produce a new zeta-zero spectrum. Quite the opposite: the only nontrivial exact selector surviving the finite-point class is the classical von Mangoldt observable already present geometrically at the anchored vertex.

No new `SOURCES.md` anchor is required for the proof: the only load-bearing facts beyond existing PC-179/PC-336 dependencies are the elementary Jensen growth argument and Chebyshev's classical lower bound, both derived or standard at the level used here. The exponential-polynomial survey above is a novelty-boundary check, not an imported theorem on which the result depends.

## 6. Consequence and surviving frontier

PC-335 and PC-336 left open the possibility that a singular symbol supported at finitely many nonendpoint Mellin frequencies could restore exact prime-power selectivity while retaining more spectral information than endpoint evaluation. Equations (7) and (32) close that branch.

For a fixed vertical Mellin line, the finite point-supported architecture has only two outcomes:

\[
\boxed{
\text{semiprime-null finite-point readout}
\Longrightarrow
\begin{cases}
0,&\sigma\neq1,\\
c\Lambda,&\sigma=1.
\end{cases}}
\tag{40}
\]

Therefore moving a finite collection of deltas or delta derivatives away from `s=1`, adding several such frequencies, or placing them at zeta zeros does not create a new exact selector. Zeta-zero support can at most generate components killed by the universal envelope and hence invisible to every shell.

The result does **not** rule out infinite or continuous Mellin support, generalized analytic functionals beyond ordinary finite-support distributions, shell-dependent singular symbols, nonlinear radial operations, non-scalar refinement cocycles, or genuinely cross-shell coupling before the final readout. Those remain outside the theorem. It also does not supply a functional equation, critical-line positivity, or a Hilbert--Polya operator; it is a negative architecture classification.

## Audit / falsification tests

A counterexample to the theorem would consist of a fixed `sigma>0`, a finite point-supported distribution `T` on that Mellin line, and exact semiprime nulls `L_T(pq)=0` for all distinct primes, together with either:

- `sigma!=1` and some shell `n` with `L_T(n)!=0`; or
- `sigma=1` and a shell response not proportional to `Lambda(n)`.

The first possibility would force a nonzero finite exponential polynomial `F_p` with at least `pi(e^R)` real zeros below scale `R`, contradicting its Jensen `O(R)` zero count. The second would leave a highest generalized-von-Mangoldt term `Lambda_R`, `R>=2`, whose semiprime specialization is a nonzero polynomial in `log q` with infinitely many roots.

## Provenance

- **Inputs:** PC-179 exact signed radial-flux Mellin factorization; PC-335 bounded indefinite Mellin no-go; PC-336 endpoint distribution classification; canonical prime-circle mandate.
- **Evidence:** exact derivation, direct Jensen zero count, classical Chebyshev prime-density bound, and a directed exponential-polynomial prior-art audit.
- **Scope:** original prime-circle radial/cyclotomic geometry only; no downstream hyperbolic construction is used.
