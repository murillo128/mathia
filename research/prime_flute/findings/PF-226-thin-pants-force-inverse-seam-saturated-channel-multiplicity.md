# PF-226 — thin pants force inverse-seam saturated channel multiplicity

**Status:** `EXACT-DERIVED + GEOMETRIC-COUNTING + NEGATIVE/ROUTE-NARROWING`. PF-225 shows that resolvent dressing caps each one-cut transmission singular value at `1/2`, so the divergent **amplitude** of the raw normalized pant crossing from PF-215/PF-224 is no longer itself an obstruction. The remaining raw quantity in PF-225's strongest one-cut estimate is the saturated channel mass

\[
\mathfrak c_n
=\sum_k\min\{1/2,s_k(B_n)\},
\qquad
B_n=\Pi_{n+1}K\Pi_n.
\]

The actual canonical thin pant already forces this channel count to grow. There are constants `\tau,c>0` such that, after a finite head,

\[
\boxed{
N_{B_n}(\tau)\ge \frac{c}{s_n},
\qquad
s_n=\frac{h_n+h_{n+1}}2,
}
\]

and hence

\[
\boxed{
\mathfrak c_n\ge \frac{c}{s_n}
\asymp
c\frac{P_n}{g_n+g_{n+1}}.
}
\]

The proof is a finite-dimensional variational band argument on the same fixed central Fermi corridor used by PF-215/PF-216. Instead of testing only the symmetric constant boundary mode, use the first `m_n\asymp s_n^{-1}` tangential Dirichlet modes on a fixed window. Opposite data across the two pant-facing boundaries cost `\gtrsim s_n^{-1}` per `L^2` unit, while same-sign data in that band cost only `O(\eta^2s_n^{-1})` after choosing the band edge `m_n\le\eta/s_n`. Polarization therefore gives a uniformly coercive cross-DtN form on an `m_n`-dimensional space. The PF-205 strip normalization costs at most `O(w_ns_n^{-2})` on the same band, and because `w_n\asymp P_n^{-1}` while `s_n\gtrsim P_n^{-1}`, the normalized crossing has at least `m_n` singular values above one fixed threshold.

Thus the actual prime-flute geometry realizes the **growing effective transport multiplicity** that PF-223 had only exhibited abstractly. This does **not** prove that the dressed cut flux `X_n=(1-E_n)DE_n`, `[D,\Omega]`, or `P[D,\Omega]H` fails weak trace class: PF-225's inverse factors can still suppress these raw channels. It does show that a successful endpoint argument cannot treat the pant crossing as a uniformly finite-channel perturbation, and it cannot close the PF-225 budget merely by capping each raw channel separately. The next positive theorem must quantify how `D`, the physical low/high projections, or both remove most of this inverse-seam raw multiplicity before the reciprocal-prime layers are summed.

## Claim

Use the simultaneous PF-205 natural-width seam cut and the notation of PF-214--PF-225. Let

\[
K=\Lambda_Q^{-1/2}\Lambda_E\Lambda_Q^{-1/2}\ge0
\]

on the normalized boundary-energy space

\[
\mathcal B=\bigoplus_{j\ge1}\mathcal B_j,
\]

and let

\[
B_n:=\Pi_{n+1}K\Pi_n
\tag{1}
\]

be the unique oriented normalized exterior crossing through the one-cusp pant between modules `n` and `n+1`. Write

\[
s_n:=\operatorname{dist}(C_n,C_{n+1})
=\frac{h_n+h_{n+1}}2
\tag{2}
\]

for the exact finite-finite common-perpendicular scale and

\[
w_j=\kappa d_j
\tag{3}
\]

for the PF-205 signed Fermi-area halfwidth of the `j`th seam strip.

There exist constants

\[
T>0,\qquad \eta>0,\qquad \tau>0,\qquad c>0
\tag{4}
\]

independent of `n` such that, after a finite head, there is an `m_n`-dimensional subspace

\[
\mathcal F_n\subset\mathcal B_n,
\qquad
m_n=\left\lfloor\frac{\eta}{s_n}\right\rfloor,
\tag{5}
\]

with

\[
\boxed{
\|B_nf\|\ge \tau\|f\|
\qquad(f\in\mathcal F_n).
}
\tag{6}
\]

Since the fixed pant crossing is smoothing and therefore compact, the singular-value min-max principle gives

\[
\boxed{
s_{m_n}(B_n)\ge\tau,
\qquad
N_{B_n}(\tau/2)\ge m_n.
}
\tag{7}
\]

In particular PF-225's saturated channel mass satisfies

\[
\boxed{
\mathfrak c_n
:=\sum_{k\ge1}\min\{1/2,s_k(B_n)\}
\ge c\,m_n
\ge \frac{c}{s_n}.
}
\tag{8}
\]

For the canonical prime parameters of PF-205/PF-215,

\[
P_n=p_{n-1},
\qquad
g_n=p_n-p_{n-1},
\tag{9}
\]

we have

\[
w_n\asymp P_n^{-1},
\qquad
s_n\asymp\frac{g_n+g_{n+1}}{P_n},
\tag{10}
\]

and therefore

\[
\boxed{
N_{B_n}(\tau/2)
\ge
c\frac{P_n}{g_n+g_{n+1}},
\qquad
\mathfrak c_n
\ge
c\frac{P_n}{g_n+g_{n+1}}.
}
\tag{11}
\]

Consequently the **strong trace-class sufficient criterion** isolated by PF-225,

\[
\sum_n\delta_n\mathfrak c_n<\infty,
\qquad
\delta_n=\frac1{P_n}-\frac1{P_{n+1}},
\tag{12}
\]

must at minimum pay

\[
\boxed{
\delta_n\mathfrak c_n
\ge
c\frac{g_n}{P_n(g_n+g_{n+1})}
}
\tag{13}
\]

on the tail. No convergence or divergence assertion for the series on the right is made here. Equation (13) is a lower diagnostic for PF-225's **raw saturated-mass sufficient route**, not a necessary condition for weak trace class of the dressed physical remainder.

## 1. A fixed central window has thickness comparable to `s_n`

PF-215 gives the exact Fermi graph of the neighboring cuff-axis over `C_n`, and PF-216 shows that after removing the PF-205 artificial seam strips the remaining pant-core ray length `\ell_n(t)` satisfies, on the growing corridor,

\[
c\,s_n\cosh t
\le
\ell_n(t)
\le
C\,s_n\cosh t.
\tag{14}
\]

Fix once a finite `T>0`. Since `s_n\to0`, the interval

\[
I=(-T,T)
\tag{15}
\]

lies inside that corridor and inside one cuff fundamental segment for every sufficiently large `n`. Thus

\[
\boxed{
c_Ts_n\le\ell_n(t)\le C_Ts_n
\qquad(t\in I).}
\tag{16}
\]

The normal-ray map from the `n`-side artificial boundary window to the `(n+1)`-side window has uniformly bounded Jacobian and inverse Jacobian on this fixed window. This is the fixed-`T` specialization of the boundary-offset control in PF-216: the derivative of the signed-distance defining function stays uniformly away from zero there. Denote the induced boundary identification by `J_n`. After changing constants,

\[
\|J_n\phi\|_{L^2}\asymp\|\phi\|_{L^2},
\qquad
\|\partial_t(J_n\phi)\|_{L^2}
\le C\bigl(\|\phi'\|_{L^2}+\|\phi\|_{L^2}\bigr).
\tag{17}
\]

Only these fixed-window comparisons are used below; no global Fourier separation of the pant is assumed.

## 2. An inverse-seam-dimensional band has a coercive cross-DtN form

Let `S_n\subset H_0^1(I)` be the span of the first

\[
m_n=\left\lfloor\eta/s_n\right\rfloor
\tag{18}
\]

Dirichlet eigenfunctions of `-\partial_t^2` on `I`, where `\eta>0` will be fixed sufficiently small. For every `\phi\in S_n`,

\[
\|\phi'\|_2
\le C_T\frac{\eta}{s_n}\|\phi\|_2.
\tag{19}
\]

Let `\mathcal E_n(a,b)` denote the minimized positive-shift `\Delta+1` energy in the pant core with boundary data `a` and `b` on the two finite artificial boundaries and zero data on the unused portions when appropriate. Put

\[
E_-(\phi):=\mathcal E_n(\phi,-J_n\phi),
\qquad
E_+(\phi):=\mathcal E_n(\phi,J_n\phi).
\tag{20}
\]

For **opposite** data, every admissible extension changes by `2\phi(t)` along the normal ray joining the paired boundary points. Weighted Cauchy--Schwarz on each ray, followed by (16), gives

\[
\boxed{
E_-(\phi)
\ge \frac{c}{s_n}\|\phi\|_2^2.
}
\tag{21}
\]

For **same-sign** data, take the trial function which is constant along each joining ray, equal to `\phi(t)`, and zero outside the fixed corridor. Because `\phi\in H_0^1(I)`, this glues as an admissible `H^1` trial function. The metric coefficients are uniformly bounded on the fixed window and the transverse thickness is `O(s_n)`, so

\[
E_+(\phi)
\le
Cs_n\bigl(\|\phi'\|_2^2+\|\phi\|_2^2\bigr)
\le
C\left(\frac{\eta^2}{s_n}+s_n\right)\|\phi\|_2^2.
\tag{22}
\]

Choose `\eta` so small that the first term in (22) is at most one quarter of the constant in (21), then take the tail far enough that the `Cs_n` term has the same property. Hence

\[
E_-(\phi)-E_+(\phi)
\ge
\frac{c}{s_n}\|\phi\|_2^2.
\tag{23}
\]

Write `\beta_n` for the exterior DtN cross form between the two pant-facing boundary components. Polarization gives

\[
E_+(\phi)=A_n(\phi)+C_n(J_n\phi)+2\beta_n(\phi,J_n\phi),
\]

\[
E_-(\phi)=A_n(\phi)+C_n(J_n\phi)-2\beta_n(\phi,J_n\phi).
\tag{24}
\]

Therefore

\[
\boxed{
-\beta_n(\phi,J_n\phi)
\ge
\frac{c}{s_n}\|\phi\|_2^2
\qquad(\phi\in S_n).
}
\tag{25}
\]

PF-215 is the `m_n=1` constant-mode shadow of this estimate. Equation (25) shows that the thin corridor carries an entire tangential band of strongly coupled channels before normalization.

## 3. PF-205 strip normalization leaves a fixed singular-value threshold

For `\phi\in S_n`, prescribe the same profile on both sides of the `n`th seam strip, using the zero-twist seam origin exactly as in PF-217. Denote this two-sided physical boundary datum by `\Phi_n(\phi)`. The constant-in-normal-coordinate strip extension is admissible in the PF-205 metric

\[
g=\frac{dx^2}{1+x^2}+(1+x^2)dt^2,
\qquad |x|<w_n,
\tag{26}
\]

so its positive-shift energy gives

\[
\begin{aligned}
q_n(\phi)
&:=\langle\Phi_n(\phi),\Lambda_{Q,n}\Phi_n(\phi)\rangle\\
&\le
Cw_n\bigl(\|\phi'\|_2^2+\|\phi\|_2^2\bigr)\\
&\le
Cw_n\left(1+\frac{\eta^2}{s_n^2}\right)\|\phi\|_2^2.
\end{aligned}
\tag{27}
\]

The paired datum `\Phi_{n+1}(J_n\phi)` satisfies the analogous estimate with `w_{n+1}` by (17). Define normalized boundary-energy vectors

\[
f_n(\phi)=\Lambda_{Q,n}^{1/2}\Phi_n(\phi),
\qquad
f_{n+1}(\phi)=\Lambda_{Q,n+1}^{1/2}\Phi_{n+1}(J_n\phi).
\tag{28}
\]

The map `\phi\mapsto f_n(\phi)` is injective because the shifted strip DtN form is positive. Module locality and the definition of `B_n` give the exact cross identity

\[
\boxed{
\langle f_{n+1}(\phi),B_nf_n(\phi)\rangle
=
\beta_n(\phi,J_n\phi).
}
\tag{29}
\]

For large `n`, the derivative term dominates the harmless `1` in (27). Combining (25), (27), and Cauchy--Schwarz yields

\[
\frac{\|B_nf_n(\phi)\|}{\|f_n(\phi)\|}
\ge
c\frac{s_n}{\sqrt{w_nw_{n+1}}}
\qquad(0\ne\phi\in S_n),
\tag{30}
\]

where the fixed choice of `\eta` has been absorbed into `c`.

Now PF-205 gives

\[
w_n=\kappa d_n,
\qquad
d_n=P_n^{-1}(1+o(1)),
\tag{31}
\]

while PF-205/PF-215 give

\[
h_n=\frac{g_n}{P_n}(1+o(1)),
\qquad
\frac{P_{n+1}}{P_n}\to1.
\tag{32}
\]

Since every odd-prime gap is at least two,

\[
s_n=\frac{h_n+h_{n+1}}2
\ge \frac{c}{P_n}
\tag{33}
\]

and therefore

\[
\boxed{
\frac{s_n}{\sqrt{w_nw_{n+1}}}\ge c_0>0.
}
\tag{34}
\]

Equations (30)--(34) prove (6). The dimension of `f_n(S_n)` is exactly `m_n`, so the compact-operator min-max principle gives (7).

Finally (32) also gives

\[
s_n\asymp\frac{g_n+g_{n+1}}{P_n},
\tag{35}
\]

which proves (11). With

\[
\delta_n
=\frac{g_n}{P_nP_{n+1}}
\asymp\frac{g_n}{P_n^2},
\tag{36}
\]

(13) follows.

## 4. What the count does and does not say about the dressed flux

PF-225 factors the actual one-cut resolvent block as

\[
X_n
=-(F_nDF_n)B_n(E_nD^{(n)}E_n),
\qquad
D=(I+K)^{-1},
\tag{37}
\]

and proves

\[
s_k(X_n)\le\min\{1/2,s_k(B_n)\}.
\tag{38}
\]

The present lower bound is deliberately on the **raw** middle factor `B_n`. It cannot be pushed through the two positive contractions in (37) without lower control on those contractions over the same `m_n`-dimensional band. PF-217 is a warning against assuming such control from the raw constant-sector mass: tangential screening can strongly change the shorted low form.

Thus (8) has two precise consequences and one precise non-consequence.

First, the uniformly finite-channel specialization of PF-225 is false in the canonical flute: the number of raw channels already above one fixed saturation threshold tends to infinity at least as `s_n^{-1}`. Second, any attempt to prove PF-225's strong criterion (12) by a bound that charges raw saturated channels must confront the arithmetic lower cost (13). But the theorem does **not** give a lower bound on `s_k(X_n)`, does not imply divergence of (12), and does not obstruct a weak-`S_1` theorem in which the inverse factors or the physical `P/H` placement suppress most raw channels.

This sharpens the live target: estimate the singular values **after** the decoupled-resolvent contractions, or prove a frequency-dependent lower bound on those contractions if the goal is a negative result. Counting raw crossing channels alone has now been pushed as far as the thin-pant geometry allows without that inverse information.

## 5. Prior art and novelty audit

No novelty is claimed for the general principles used in the proof. Variational Dirichlet-to-Neumann forms, polarization, fixed-window thin-channel estimates, and singular-value min-max are standard.

Hislop and Lutzer, *Spectral Asymptotics of the Dirichlet-To-Neumann Map on Multiply Connected Domains in R^d*, **Inverse Problems 17** (2001), 1717--1741, DOI `10.1088/0266-5611/17/6/313`, prove in a fixed smooth multiply connected domain that the DtN map is a direct sum of componentwise operators plus a smoothing remainder. That is consistent with PF-222's fixed-pant smoothing statement but supplies no uniform singular-value count when the distance between the relevant components collapses.

Bucur, Henrot, and Michetti, *Asymptotic behaviour of the Steklov spectrum on dumbbell domains*, **Communications in Partial Differential Equations 46** (2021), 362--393, DOI `10.1080/03605302.2020.1840587`, study Steklov spectral degeneration in domains joined by a vanishing thin tube. It confirms that thin-domain Steklov problems can acquire nontrivial lower-dimensional spectral limits, but its geometry and eigenvalue problem do not give the normalized off-diagonal pant-crossing count (7).

A targeted search of DtN/Steklov thin-domain and multiply-connected-domain literature did not identify a theorem that directly yields the canonical PF statement `N_{B_n}(\tau)\gtrsim s_n^{-1}` with the PF-205 boundary-energy normalization. The durable project-specific deduction is therefore not a claim of a new general thin-domain theorem: it is the explicit specialization of the elementary thin-corridor band argument to the exact prime-flute pant geometry, followed by the PF normalization and PF-225 saturated-channel currency.

## 6. Falsification and boundary checks

1. The argument uses only a fixed tangential window, so it does not assume that the entire long cuff is uniformly `O(s_n)` from its neighbor.
2. The same-sign trial estimate is valid because the band lies in `H_0^1(I)`; no discontinuous cutoff at the window edge is introduced.
3. The opposite-sign estimate is a lower bound for the minimized `\Delta+1` energy, not for one chosen extension. The positive `L^2` term can only increase it.
4. The zero-twist marking is load-bearing for using the same tangential profile on both sides of each PF-205 strip without an inverse-width welding cost, exactly as in PF-217.
5. Equation (27) is an upper bound on strip normalization, which is the direction needed for the lower bound (30). No unproved lower asymptotic for nonconstant strip modes is used.
6. The threshold in (34) uses only the exact PF scales `w_n\asymp P_n^{-1}` and `s_n\gtrsim P_n^{-1}`; it does not require a statistical law for consecutive prime-gap ratios.
7. The count concerns `B_n`, not `X_n=[D,E_n]` or the physical `P[D,\Omega]H`. PF-225's resolvent contractions may strongly reduce the raw band.
8. The lower series in (13) is not asserted to diverge. Even failure of PF-225's strong trace-class sufficient criterion would not by itself rule out the desired weak-`S_1` endpoint.
9. Nothing here addresses PF-204's unsmoothed mixed transport, PF-183's true short-collar splice, prime/clone separation, wave operators, determinants/resonances, or an RH implication.

## Consequences for the research line

PF-223 identified uncontrolled transport multiplicity as the abstract way compact cut flux can miss weak trace class. PF-224 showed that one raw canonical pant channel is already too large for amplitude-only summation. PF-225 then showed that resolvent dressing saturates that amplitude and moved the frontier to channel count. PF-226 now establishes that the **raw canonical** crossing indeed carries a growing inverse-seam number of saturated channels.

The smooth weak-trace route is therefore no longer a raw pant estimate. A positive continuation should place the PF-212 physical-frequency splitting *inside* the dressed factorization (37), or otherwise prove that `F_nDF_n` and `E_nD^{(n)}E_n` suppress all but a reciprocal-prime-summable portion of the band from (7). A negative continuation must do the opposite: prove that a sufficiently large subspace of this band survives both resolvent contractions and the physical low/high placement. The unsmoothed PF-204 route and the independent PF-183 true-short-collar splice remain separate live alternatives.