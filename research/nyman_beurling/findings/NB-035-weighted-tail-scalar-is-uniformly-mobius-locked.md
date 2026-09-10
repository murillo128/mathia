# NB-035 — the weighted tail scalar is uniformly locked to a reciprocal-Möbius partial sum

**Status:** `EXACT-DERIVED + TARGET-SELECTED-TAIL-AGGREGATE + UNIFORM-IN-CUTOFF-STABILITY + ARBITRARY-APPROXIMANT-TAIL-SELECTOR + EXPLICIT-UNIFORM-DUAL-CERTIFICATE + RECIPROCAL-MOBIUS-DISTANCE-FLOOR + CLASSICAL-PNT-COROLLARY + METHOD-BOUNDARY`. `NB-034` constructs the source-faithful weighted-tail quotient

\[
\widehat W_{M,N}=\operatorname{span}\bigl(ng_n-(n+1)g_{n+1}:M\le n<N\bigr)
\]

and shows that the best canonical coefficient vector

\[
P_{V_N}e=\sum_{n=2}^N a_{N,n}g_n
\]

survives in the quotient through every head coefficient `a_{N,n}`, `n<M`, together with the single endpoint coordinate

\[
\tau_{M,N}:=M\sum_{n=M}^N\frac{a_{N,n}}n.
\tag{1}
\]

That endpoint was previously only known to be the source coordinate retained by the quotient; it could still have behaved like an uncontrolled global tail parameter. It is in fact rigidly selected by the same small residual that locks the head coefficients to Möbius values.

Let

\[
r_N=e-P_{V_N}e,
\qquad d_N=\|r_N\|,
\qquad
m(L):=\sum_{k\le L}\frac{\mu(k)}k.
\tag{2}
\]

Then for **every** pair of integers `2 <= M <= N`,

\[
\boxed{
\left|
\frac{\tau_{M,N}}M-m(M-1)
\right|
=
\left|
\sum_{n=M}^N\frac{a_{N,n}}n
-
\sum_{k\le M-1}\frac{\mu(k)}k
\right|
\le C_* d_N,
}
\tag{3}
\]

where the absolute constant may be taken as

\[
\boxed{
C_*:=\sqrt{4+20\zeta(2)}<7.
}
\tag{4}
\]

The decisive feature is that the constant in (3) is independent of **both** `M` and `N`. Thus the weighted-tail scalar from `NB-034` is not a free coordinate whose stability deteriorates with the retained dimension.

A classical PNT consequence gives `m(L)->0`. Therefore, along any subsequence on which `d_N->0`, every independently chosen cutoff `M_N<=N` with `M_N->infinity` satisfies

\[
\boxed{
\frac{\tau_{M_N,N}}{M_N}
=
\sum_{n=M_N}^N\frac{a_{N,n}}n
\longrightarrow0.
}
\tag{5}
\]

For fixed `M`, the same estimate instead gives

\[
\frac{\tau_{M,N}}M\longrightarrow m(M-1)
\qquad(d_N\to0).
\tag{6}
\]

Equations (5)--(6) expose a two-scale source law for the sole weighted-tail degree of freedom: fixed cutoffs converge to the corresponding finite reciprocal-Möbius sum, while every growing cutoff converges to zero after the quotient's natural `1/M` normalization.

The bounded endpoint functional has a stronger interpretation that was not made explicit in the first version of this finding. It is the Riesz representer of an exact **step-tail selector**: for every cutoff `L`, it annihilates all generators `g_2,...,g_L`, pairs with every later generator `g_n` as exactly `1/n`, and pairs with the target as `m(L)`, while its Hilbert norm stays bounded by the same absolute constant `C_*`. Consequently (3) is only the best-approximant specialization of an arbitrary-approximant inequality, and the empty-tail case gives the explicit source-side distance floor `|m(N)| <= C_* d_N`. Section 4 derives this dual form without adding any analytic hypothesis.

## 1. The `NB-034` endpoint functional is the exact tail coordinate

Put `L=M-1`. For `1<=d<=L`, define

\[
a_d:=\left\lfloor\frac Ld\right\rfloor,
\qquad
m(q):=\sum_{k\le q}\frac{\mu(k)}k,
\qquad
q_d:=\frac{m(a_d)}d.
\tag{7}
\]

`NB-034` proves the following exact endpoint identity. If a retained coefficient vector is written as `c=(c_2,...,c_M)` and its first `L` shell values are

\[
v_t=\sum_{j=2}^M c_j\left\{\frac tj\right\},
\qquad v_0=0,
\]

then

\[
\boxed{
\frac{c_M}{M}
=
\sum_{d=1}^L q_d\,(v_d-v_{d-1}).
}
\tag{8}
\]

For the canonical weighted quotient, `c_j=a_{N,j}` for `j<M` and `c_M=\tau_{M,N}`. The discarded weighted tail vanishes on every shell `I_t`, `t<M`, so the quotient approximant has exactly the same early-shell values as the full best approximant:

\[
v_t=1-r_{N,t}
\qquad(1\le t\le L),
\tag{9}
\]

where `r_{N,t}` is the constant value of `r_N` on `I_t`.

Substituting (9) into (8) gives

\[
\frac{\tau_{M,N}}M
=
m(L)
-
\left(
q_1r_{N,1}
+
\sum_{d=2}^Lq_d(r_{N,d}-r_{N,d-1})
\right),
\tag{10}
\]

because `q_1=m(L)`. Hence (3) is reduced to a uniform norm bound for one explicit finite functional of the early residual.

## 2. The reciprocal-Möbius endpoint functional has an absolute Hilbert norm

The key cancellation is elementary. The divisor identity

\[
\sum_{k\le q}\mu(k)\left\lfloor\frac qk\right\rfloor=1
\]

implies

\[
q\,m(q)
=
1+
\sum_{k\le q}\mu(k)\left\{\frac qk\right\}.
\tag{11}
\]

Therefore

\[
\boxed{|m(q)|\le1\qquad(q\ge1).}
\tag{12}
\]

Now set

\[
D_t:=m(a_t)-m(a_{t+1})
=
\sum_{a_{t+1}<k\le a_t}\frac{\mu(k)}k
\qquad(1\le t<L).
\tag{13}
\]

The intervals in (13) are pairwise disjoint. If `t<=sqrt(L)`, then

\[
a_t-a_{t+1}
\le\frac{L}{t(t+1)}+1,
\]

while every integer in the block is larger than `L/(t+1)`. Hence

\[
|D_t|
\le\frac1t+\frac{t+1}{L}
\le\frac3t.
\tag{14}
\]

If `t>sqrt(L)`, the two floors differ by at most one, so a nonempty block contains a single reciprocal integer. Disjointness then gives

\[
\sum_{t<L}|D_t|^2
\le9\sum_{t\ge1}\frac1{t^2}
+
\sum_{k\ge1}\frac1{k^2}
=10\zeta(2).
\tag{15}
\]

Discrete summation by parts rewrites the residual functional in (10) as

\[
q_Lu_L+
\sum_{t=1}^{L-1}(q_t-q_{t+1})u_t,
\qquad u_t:=r_{N,t},\quad u_0:=0.
\tag{16}
\]

The coefficient difference has the exact decomposition

\[
q_t-q_{t+1}
=
\frac{m(a_t)}{t(t+1)}
+
\frac{D_t}{t+1}.
\tag{17}
\]

Using (12), (15), `|x+y|^2<=2|x|^2+2|y|^2`, and `q_L=1/L`, the squared dual norm with respect to the harmonic-shell weights obeys

\[
\begin{aligned}
S_L
&:=
\sum_{t=1}^{L-1}
 t(t+1)|q_t-q_{t+1}|^2
+L(L+1)|q_L|^2\\
&\le
2\sum_{t=1}^{L-1}\frac1{t(t+1)}
+2\sum_{t=1}^{L-1}|D_t|^2
+\frac{L+1}{L}\\
&\le4+20\zeta(2).
\end{aligned}
\tag{18}
\]

This bound is uniform in `L`. Cauchy--Schwarz in the shell weights now gives

\[
\left|
q_1r_{N,1}
+
\sum_{d=2}^Lq_d(r_{N,d}-r_{N,d-1})
\right|^2
\le
S_L
\sum_{t=1}^L\frac{|r_{N,t}|^2}{t(t+1)}.
\tag{19}
\]

The early-shell sum in (19) is at most the full residual norm `d_N^2`. Equations (10), (18), and (19) prove (3)--(4). No prime number theorem, zero-free region, Gram inversion estimate, or assumption on `d_N` enters this finite inequality.

The edge case `M=2` is included: then `L=1`, `\tau_{2,N}/2=\sum_{n=2}^N a_{N,n}/n=1-r_{N,1}`, and `m(1)=1`, so (3) reduces to the first-shell residual estimate.

## 3. What the estimate adds to the source-faithful skeleton

`NB-020` shows that small `d_N` locks each low coefficient to `-\mu(n)` with

\[
|a_{N,n}+\mu(n)|\le2d_N\sigma(n).
\tag{20}
\]

That coordinatewise bound becomes expensive if one simply sums it over a long head. Equation (3) is different: after the weighted quotient has compressed the whole block `M,...,N` to one harmonic aggregate, the aggregate has an **absolute** `O(d_N)` stability constant. The divisor/floor organization in (8) cancels the apparent growth from summing the individual coefficient errors.

Consequently all source coordinates retained by the `NB-034` skeleton now carry an arithmetic constraint selected by the target residual. The head coordinates obey the local Möbius locking (20), while the only tail coordinate obeys the global but uniformly stable law (3). This is stronger than merely knowing that the quotient preserves the distance and is polynomially conditioned: its final coordinate is itself source-rigid.

The PNT corollary (5) uses only the classical limit

\[
\sum_{k\le x}\frac{\mu(k)}k\longrightarrow0.
\tag{21}
\]

It is deliberately separated from the exact finite statement. In particular, (3) does not assume RH and does not use a quantitative Mertens estimate.

## 4. The same functional is an exact bounded step-tail dual selector

The endpoint functional can be represented inside the ambient Hilbert space, not only as a coordinate identity on a weighted quotient. Fix an integer `L>=1`, use the numbers `q_t` from (7), and set `q_{L+1}:=0`. With

\[
I_t=\left(\frac1{t+1},\frac1t\right],
\]

define the explicit early-shell vector

\[
\boxed{
\Psi_L(x):=
\sum_{t=1}^{L}
 t(t+1)(q_t-q_{t+1})\,\mathbf 1_{I_t}(x).
}
\tag{22}
\]

For any `f in L^2(0,1)`, let

\[
A_t(f):=t(t+1)\int_{I_t}f(x)\,dx
\]

be its shell average. Then

\[
\langle f,\Psi_L\rangle
=
\sum_{t=1}^{L}(q_t-q_{t+1})A_t(f).
\tag{23}
\]

The arithmetic normalization of the selector is exact:

\[
\sum_{t=1}^{L}q_t
=
\sum_{tk\le L}\frac{\mu(k)}{tk}
=
\sum_{r\le L}\frac1r\sum_{k\mid r}\mu(k)
=1.
\tag{24}
\]

On every shell `I_t`, the canonical generator has average `A_t(g_n)={t/n}`. Summation by parts and (24) therefore give the complete pairing law

\[
\boxed{
\langle e,\Psi_L\rangle=m(L),
\qquad
\langle g_n,\Psi_L\rangle=
\begin{cases}
0,&2\le n\le L,\\[2mm]
1/n,&n\ge L+1.
\end{cases}
}
\tag{25}
\]

For the second line, if `n>L` then `{t/n}=t/n` throughout the support and

\[
\sum_{t=1}^{L}t(q_t-q_{t+1})
=
\sum_{t=1}^{L}q_t=1.
\]

If `2<=n<=L`, discrete differentiation gives

\[
\begin{aligned}
\langle g_n,\Psi_L\rangle
&=
\sum_{t=1}^{L}q_t
\left(
\left\{\frac tn\right\}
-
\left\{\frac{t-1}{n}\right\}
\right)\\
&=
\frac1n-
\sum_{r\le L/n}q_{nr}.
\end{aligned}
\]

Writing `Q=floor(L/n)` and using `floor(L/(nr))=floor(Q/r)`, the last sum is

\[
\sum_{r\le Q}q_{nr}
=
\frac1n
\sum_{r\le Q}
\frac{m(\lfloor Q/r\rfloor)}r
=
\frac1n,
\]

where the final identity is exactly (24) with `L` replaced by `Q`. This proves (25) directly from finite divisor inversion; no quotient geometry or best-approximation normal equation is needed.

The Hilbert norm of the selector is precisely the dual shell norm already estimated in (18):

\[
\boxed{
\|\Psi_L\|^2
=
\sum_{t=1}^{L}t(t+1)|q_t-q_{t+1}|^2
=S_L
\le C_*^2.
}
\tag{26}
\]

Thus, for **arbitrary** coefficients `a_2,...,a_N`, every `1<=L<=N`, and

\[
v_N=\sum_{n=2}^{N}a_ng_n,
\qquad r=e-v_N,
\]

the exact pairings (25) and Cauchy--Schwarz give the uniform approximation inequality

\[
\boxed{
\left|
 m(L)-\sum_{n=L+1}^{N}\frac{a_n}{n}
\right|
=
|\langle r,\Psi_L\rangle|
\le C_*\|r\|.
}
\tag{27}
\]

The sum is empty when `L=N`. Taking the infimum over every approximant in `V_N` then produces an explicit source-side lower bound for the canonical finite Nyman distance:

\[
\boxed{
|m(N)|\le C_*d_N,
\qquad
 d_N\ge\frac1{C_*}
\left|\sum_{k\le N}\frac{\mu(k)}k\right|.
}
\tag{28}
\]

Equivalently, `\Psi_N` is a completely explicit norm-bounded dual certificate:

\[
\Psi_N\in V_N^\perp,
\qquad
\langle e,\Psi_N\rangle=m(N),
\qquad
\|\Psi_N\|\le C_*.
\tag{29}
\]

This also clarifies the original tail statement. Taking `L=M-1` in (27) and the canonical best approximant recovers (3) exactly, while `L=N` is the previously unstated empty-tail endpoint. The weighted-tail locking and the dual distance certificate are therefore two faces of the same finite selector, not separate mechanisms.

The edge case `L=1` is explicit: `q_1=1`, so `\Psi_1=2\mathbf 1_{I_1}`, it annihilates the empty space `V_1`, pairs with every `g_n`, `n>=2`, as `1/n`, and has squared norm `2`.

## 5. Prior-art and adversarial boundary

The Möbius role in the Nyman--Beurling/Báez-Duarte program is classical. Báez-Duarte's strengthening and arithmetical formulations use Möbius inversion and natural Möbius-coefficient approximants, while Bettin--Conrey--Farmer study a mollified Möbius Dirichlet polynomial in the conditional optimal-asymptotic problem. The PNT consequence (21) is likewise classical. Generic Hilbert-space duality, orthogonal complements, and biorthogonal systems are also standard parts of the Nyman literature. This finding makes no novelty claim for any of those facts.

A targeted literature check covered Báez-Duarte's arithmetical and discrete formulations, the Bettin--Conrey--Farmer optimal-polynomial work, finite Gram analyses, and Hardy-space orthogonality/biorthogonality work, together with searches for finite optimal-coefficient or dual identities involving reciprocal Möbius sums. It did not locate either the cutoff-uniform best-approximant estimate (3) or the explicit finite shell-supported selector (22)--(29) with the exact head/tail pairing law (25). Search absence is not a priority claim; the mathematical delta asserted here is only the exact finite consequence of the canonical shell system and the bounded reciprocal-Möbius functional established inside this line. No new external quantitative estimate is load-bearing, so `SOURCES.md` is unchanged.

Several controls remain important. First, neither (3) nor (28) upper-bounds `d_N`; using (5) requires a closure subsequence `d_N->0`, so none of these inequalities can be fed back as a proof of RH without an independent coercive estimate. Second, the raw endpoint coordinate `\tau_{M,N}` may still be as large as `M d_N` after subtracting `M m(M-1)`; only its natural normalized form `\tau/M` has the uniform error in (3). Third, for `L<N` the tail term in (27) is essential: the selector deliberately sees every later generator as `1/n`, so one cannot drop that source term and retain (28) at an earlier cutoff. Fourth, `\Psi_N` is a valid bounded dual witness but is not asserted to be the optimal dual residual, and the bound `C_*` is only the proved uniform constant, not a sharp norm asymptotic.

The new lower bound (28) is structurally informative but is not currently competitive with the zero-sensitive Burnol floor as a general asymptotic lower bound: `m(N)->0` by PNT and no lower magnitude of `m(N)` at the Burnol scale is supplied here. Its value is instead that it exposes a concrete source-selected component of the finite target obstruction. Small Nyman distance forces reciprocal-Möbius cancellation at the **same finite cutoff**, with an absolute norm conversion and no Gram inversion.

The finite functional estimate survives arbitrary growth of the cutoff because its dual shell norm is bounded absolutely. This remains the decisive falsification test: a residual factor such as `H_M`, `log M`, or a power of `M` would have left both the weighted-tail endpoint and the dual witness uncontrolled on the near-logarithmic cutoffs of `NB-034`. None remains.

## 6. Research consequence

The live boundary after `NB-034` asked whether the Möbius-locked core or the retained weighted tail scalar obeys a quantitative constraint strong enough to make the conditioned skeleton useful rather than merely faithful. Equation (3) supplies such a constraint for the tail coordinate: after normalization by `M`, it is pinned to the explicit arithmetic quantity `m(M-1)` with error at most `C_*d_N`, uniformly over every cutoff and every upper section.

The strengthened form (22)--(29) also supplies a genuinely target-aware object: a finite, explicit, uniformly norm-bounded annihilator of `V_N` whose target evaluation is the reciprocal-Möbius partial sum `m(N)`. This is the kind of source-forced dual datum sought by the accepted target-aware finite-section clue, but it does **not** resolve that clue's asymptotic requirement because the witness evaluation itself can be much smaller than the known zero-sensitive distance scale. The remaining problem is not to manufacture a bounded dual vector; it is to obtain a target evaluation, or a compatible family of evaluations, that is quantitatively coercive at a useful growing scale.

What has changed is the shape of the source/target interface. A future coercive argument no longer has to treat the weighted tail endpoint as an arbitrary global nuisance parameter, and it can work with the exact selector law (25) rather than reconstructing the tail through a poorly conditioned Gram inverse. The next useful theorem must either amplify this bounded selector family without losing target information, combine it with the retained conditioned Gram equations to force additional target mass, or prove that even these source-rigid dual channels remain asymptotically too weak.