# WI-213 — natural-scale residual survives every admissible phase lift of the two-pair screen

**Status:** `EXACT-DERIVED + CLASSICAL-IDENTITY + STRUCTURAL-RIGIDITY + LITERATURE-CONTEXT`.

WI-211 constructs two additional off-line functional-equation pairs that cancel an equal-depth arithmetic bow exactly at the two reciprocal harmonics available when `2<d<3`, and WI-212 shows that every fixed finite reciprocal packet can likewise be screened by only finitely many deep off-line pairs. The remaining question in `CLUE-two-harmonic-screen-continuum-residual` is whether the exact WI-211 screen also cancels the coherent peak between those samples once the integer phase-lift freedom is retained and the frequency window is priced in the actual source variable.

It does not. For the WI-211 two-pair family, every admissible sequence of integer lifts whose normalized continuum energy remains bounded has, after passage to a subsequence, an explicit natural-scale profile

\[
\boxed{
F_{h,\kappa,q}(u)
=2\cosh(2h)\frac{\sin(\pi u)}{\pi u}
+e^{2\pi i\kappa u}
\left[-2\cosh(2h)+\pi(3+4q)\cosh^2(h)\,u\right],
}
\tag{1}
\]

where `q` is an integer relative lift and `\kappa` is the limiting common lift divided by the bow length. Its derivative at the cancelled harmonic is

\[
\boxed{
F'_{h,\kappa,q}(0)
=\pi(3+4q)\cosh^2(h)-4\pi i\kappa\cosh(2h).
}
\tag{2}
\]

Because `3+4q` is an odd integer congruent to `3 (mod 4)`, it never vanishes. Hence

\[
\boxed{|F'_{h,\kappa,q}(0)|\ge \pi\cosh^2 h>0.}
\tag{3}
\]

The central representatives in the clue correspond to `(q,\kappa)=(0,0)` and recover its proposed slope `3\pi\cosh^2 h`. The best relative integer lift is instead `q=-1`, which reduces the leading slope by a factor `3` but cannot remove it. Thus the clue's central small-window energy coefficient is not lift-uniform: the optimal lifted leading coefficient is smaller by a factor `9`, but it remains strictly positive.

The frequency window also has an exact source dictionary. Put `L=\log T`, choose the bow-center twist `U`, and let

\[
X=T^{2/d},\qquad x_M(u)=T^{(2+u/M)/d}=X\exp\!\left(\frac{uL}{dM}\right).
\tag{4}
\]

Then the synthetic bow-plus-screen function is exactly the `x^{1/2}`-normalized selected zero-residue integrand of the twisted explicit formula at `x=x_M(u)`, up to the common harmless sign/phase. A window `u=O(1)` therefore has physical relative width

\[
\boxed{\frac{\Delta x}{X}\asymp \frac{L}{dM},}
\tag{5}
\]

which is precisely the bow/Gallagher scale already isolated in WI-195 and WI-209. For every fixed lifted limit (1), choose fixed `c>0` and sufficiently small fixed `\lambda>0` so that

\[
J_{h,\kappa,q}(c,\lambda)
:=\int_{-c}^{c-\lambda}
\left|\int_s^{s+\lambda}F_{h,\kappa,q}(v)\,dv\right|^2ds>0.
\tag{6}
\]

The selected bow-plus-screen residue in the corresponding physical short interval then has energy

\[
\boxed{
\int |Q_M(x)|^2dx
=\left(J_{h,\kappa,q}(c,\lambda)+o(1)\right)
\frac{X^2L^3}{d^3M},
}
\tag{7}
\]

whereas the raw-prime Gallagher diagonal at short length

\[
K\sim \lambda\frac{XL}{dM}
\tag{8}
\]

is

\[
XK\log X
\sim \frac{2\lambda X^2L^2}{d^2M}.
\tag{9}
\]

Consequently the selected residual remains logarithmically superdiagonal:

\[
\boxed{
\frac{\int |Q_M(x)|^2dx}{XK\log X}
=\left(\frac{J_{h,\kappa,q}(c,\lambda)}{2\lambda d}+o(1)\right)L.
}
\tag{10}
\]

This is a source-scale statement about the selected zero residue, not an unconditional contradiction for zeta. WI-195 shows that the missing theorem is still a diagonal-scale upper bound for the **full** source-fixed error in this Gallagher norm. If such a bound were available, (10) would force the entire complementary source contribution to approximate the negative of the screened-bow residual to relative `O(L^{-1/2})`, exactly as WI-209 derived for the unscreened dense bow. No published theorem audited in this line currently supplies that source upper bound. Thus the two-pair screen is now ruled out as a continuum flattening mechanism, but remote zeros, additional off-line pairs, and the structured prime-side/source terms remain possible cancellation reservoirs.

## 1. Exact central profile

Let `M` be odd and use the clue/WI-211 notation

\[
D_M(t)=\frac{\sin(\pi Mt)}{\sin(\pi t)},
\qquad
B_M(t)=2\cosh(ht)D_M(t).
\tag{11}
\]

Set

\[
A_M=\frac12M\cosh h,
\qquad
C_M=\frac12M\cosh(2h),
\tag{12}
\]

and let `y_M` be the larger root of

\[
2y^2-(4A_M^2+1+C_M)y+2A_M^2=0.
\tag{13}
\]

Define

\[
a_M=\operatorname{arcosh}\sqrt{y_M},
\qquad
\phi_M=\arccos\!\left(-\frac{A_M}{\sqrt{y_M}}\right).
\tag{14}
\]

WI-211 already proves

\[
y_M=\frac12M^2\cosh^2h+\frac14M\cosh(2h)+O_h(1),
\tag{15}
\]

so

\[
\frac{\cosh(2a_M)}{M^2}\longrightarrow\cosh^2h,
\qquad
\phi_M\longrightarrow\frac{3\pi}{4},
\qquad
a_M=\log M+O_h(1).
\tag{16}
\]

At `t=2+u/M`, the Dirichlet kernel has the exact form

\[
\frac{D_M(2+u/M)}{M}
=\frac{\sin(\pi u)}{M\sin(\pi u/M)},
\tag{17}
\]

hence uniformly for `u` in compact intervals

\[
\frac{B_M(2+u/M)}M
\longrightarrow
2\cosh(2h)\frac{\sin(\pi u)}{\pi u}.
\tag{18}
\]

For the central screen

\[
S_M(t)=4\cosh(a_Mt)\cos(\phi_Mt),
\tag{19}
\]

WI-211's root relation gives exactly

\[
S_M(2)=-2M\cosh(2h).
\tag{20}
\]

Differentiation gives a depth term of size `O_h(M\log M)` and a phase term of size `M^2`; using (16),

\[
\frac{S_M'(2)}{M^2}\longrightarrow3\pi\cosh^2h.
\tag{21}
\]

For bounded `u`, `S_M''(2+\theta u/M)=O_{h,u}(M^2\log^2M)`, so Taylor's remainder divided by `M` is `O_{h,u}(\log^2M/M)`. Combining (18)--(21) proves the clue's central profile uniformly on every compact `u`-interval:

\[
\frac{B_M(2+u/M)+S_M(2+u/M)}M
\to
2\cosh(2h)\left(\frac{\sin(\pi u)}{\pi u}-1\right)
+3\pi\cosh^2h\,u.
\tag{22}
\]

The odd linear term is orthogonal on a symmetric interval to the even sinc-minus-one term, so the clue's central bound follows exactly:

\[
\int_{-c}^{c}|F_{h,0,0}(u)|^2du
\ge6\pi^2c^3\cosh^4h.
\tag{23}
\]

## 2. Integer phase lifts cannot flatten the peak

The two WI-211 phases are fixed only modulo `2\pi`. Write general integer lifts as

\[
\theta_{+,M}=\phi_M+2\pi n_{+,M},
\qquad
\theta_{-,M}=-\phi_M+2\pi n_{-,M},
\tag{24}
\]

and

\[
S_M^{\rm lift}(t)
=2\cosh(a_Mt)
\left(e^{i\theta_{+,M}t}+e^{i\theta_{-,M}t}\right).
\tag{25}
\]

At both integer harmonics `t=1,2`, every lift has exactly the same values as the central screen. Put

\[
n_M=n_{-,M},\qquad q_M=n_{+,M}-n_{-,M}.
\tag{26}
\]

Then

\[
S_M^{\rm lift}(t)=e^{2\pi i n_Mt}H_{M,q_M}(t),
\tag{27}
\]

where

\[
H_{M,q}(t)=2\cosh(a_Mt)
\left(e^{i(\phi_M+2\pi q)t}+e^{-i\phi_Mt}\right).
\tag{28}
\]

For fixed integer `q`, (20) gives `H_{M,q}(2)=-2M\cosh(2h)`, while direct differentiation and (16) give

\[
\boxed{
\frac{H_{M,q}'(2)}{M^2}
\longrightarrow
\pi(3+4q)\cosh^2h.
}
\tag{29}
\]

If the lifts remain inside the `M`-cell bow interval, `n_M/M` is bounded (indeed it lies in `[-1/2,1/2]+o(1)` under the centered convention). Along any subsequence with

\[
q_M=q\in\mathbb Z,
\qquad
\frac{n_M}{M}\to\kappa,
\tag{30}
\]

the same uniform Taylor argument yields

\[
\frac{B_M(2+u/M)+S_M^{\rm lift}(2+u/M)}M
\longrightarrow F_{h,\kappa,q}(u)
\tag{31}
\]

with `F` given by (1).

It remains to exclude a low-energy escape with varying relative lift. If `|q_M|/M` stays bounded away from zero along a subsequence, the relative factor `e^{2\pi iq_Mu/M}` fails to approach `1` on a positive-measure set of fixed `u`, while each individual screen term has normalized size `asymp M`; the normalized `L^2` energy therefore diverges. If instead `q_M=o(M)` but `|q_M|\to\infty`, then for every fixed nonzero `u` the relative phase difference is `2\pi q_Mu/M=o(1)` but its product with the individual normalized amplitude `asymp M` has magnitude `asymp |q_Mu|`; again the normalized energy diverges by Fatou on any fixed interval avoiding `u=0`. Hence any sequence of admissible lifts with bounded normalized continuum energy has `q_M=O(1)`, and after a subsequence (30) applies.

Equation (2) follows by differentiating (1). Since

\[
|3+4q|\ge1\qquad(q\in\mathbb Z),
\tag{32}
\]

we obtain (3). In particular no bounded-energy integer lift makes the limiting profile vanish identically. For small symmetric windows,

\[
\int_{-c}^{c}|F_{h,\kappa,q}(u)|^2du
=\frac23|F'_{h,\kappa,q}(0)|^2c^3+O_{h,\kappa,q}(c^4),
\tag{33}
\]

and the smallest possible leading slope occurs at `q=-1`, `\kappa=0`, giving magnitude `\pi\cosh^2h`. Thus the central coefficient in (23) may drop by a factor `9` under an admissible relative lift, but it cannot drop to zero.

## 3. The continuum window is exactly a Gallagher-scale physical slab

Use the unfolded bow normalization from WI-209--WI-211,

\[
\frac{\gamma_jL}{2\pi}=x_0+dj,
\qquad
b_j=(\beta_j-\tfrac12)L=dh,
\tag{34}
\]

and twist at the bow center `U=2\pi x_0/L`. For a source location `x=x_M(u)` from (4), put

\[
t=\frac{d\log x}{L}=2+\frac{u}{M}.
\tag{35}
\]

Then for a selected bow mirror pair,

\[
x^{\beta_j-1/2}e^{i(\gamma_j-U)\log x}
+x^{1/2-\beta_j}e^{i(\gamma_j-U)\log x}
=2\cosh(ht)e^{2\pi ijt}.
\tag{36}
\]

For either added screen pair, an unfolded phase lift by `dn` gives exactly

\[
2\cosh(a_Mt)e^{i(\pm\phi_M+2\pi n)t}.
\tag{37}
\]

Thus `R_M(t)=B_M(t)+S_M^{lift}(t)` is not merely analogous to a source observable: after extracting the common factor `x^{-1/2}` and the common explicit-formula sign, it is exactly the selected zero-residue integrand.

Let `Q_M(s,\lambda)` be the selected residue in the twisted short interval with endpoints `x_M(s)` and `x_M(s+\lambda)`. The classical integrated explicit-formula term is

\[
Q_M(s,\lambda)
=-\int_{x_M(s)}^{x_M(s+\lambda)}x^{-1/2}R_M(t(x))\,dx.
\tag{38}
\]

Since

\[
\frac{dx_M(v)}{dv}=x_M(v)\frac{L}{dM},
\tag{39}
\]

(31) gives, uniformly for `s` in fixed compact intervals,

\[
\boxed{
\frac{Q_M(s,\lambda)}{X^{1/2}L/d}
\longrightarrow
-\int_s^{s+\lambda}F_{h,\kappa,q}(v)\,dv.
}
\tag{40}
\]

The physical short length is (8). Integrating the squared residue over a fixed `s`-window and using `dx_M/ds\sim XL/(dM)` yields (7). Since `\log X=(2/d)L`, comparison with the same raw-prime diagonal used in WI-195/WI-209 gives (10).

The positivity of `J` in (6) is automatic for sufficiently small `\lambda`: if every short moving average vanished on an interval then differentiation would force the analytic profile `F` to vanish there, contradicting (3). Moreover the admissible common-lift parameter is compact and the only low-energy relative lifts are bounded integers, so the same compactness argument gives a positive infimum after restricting to any family with bounded normalized energy. Large relative lifts already have divergent normalized residual energy and are not an escape.

## 4. What this does and does not rule out

The exact two-pair WI-211 screen can therefore cancel the first two reciprocal **samples**, but it cannot cancel the natural coherent peak around the second sample, even after optimizing the integer representatives inside the bow. In source variables the leftover peak costs the same physical resolution `K\asymp XL/M` as the Gallagher bridge and its selected zero-residue energy is `Omega(L)` times the raw-prime diagonal. A sparse exact finite-moment screen is therefore not a sparse continuum screen.

This is still not a zeta-zero exclusion. The full explicit formula contains every complementary zero and the structured source terms. A source upper bound of the form

\[
\|E_{\rm src}\|_2^2\ll XK\log X
\tag{41}
\]

on this distinguished slab would conflict with (10) unless those complementary terms form an asymptotically near-opposite vector. WI-195 records that no currently audited theorem supplies the required square-root-scale variance for the `\Lambda-\Lambda^\sharp` source error, and WI-209 already identifies the same cancellation burden for the unscreened bow. The present result shows that the exact WI-211 two-pair correction does not remove that burden.

Nor does this argument yet rule out changing the two screen depths/phases away from the WI-211 equal-depth construction, using more than two added off-line pairs, or arranging cancellation by a remote/global zero population. WI-212's finite-packet algebraic obstruction therefore remains valid: finitely many discrete samples alone do not charge the sparse screen. What changes is that one natural continuum refinement survives all phase lifts of the explicit two-pair screen and lands at the correct source scale.

## 5. Prior-art and novelty audit

The ingredients used here are separated by provenance. The identity (17) and its sinc scaling are classical Dirichlet-kernel/Fourier-series facts. The integrated zero residue (38) is the classical explicit-formula identity already used in WI-205/WI-209. The short-interval `L^2`/Gallagher scale and the currently missing source variance theorem were audited in WI-195; weighted Gallagher variants are classical prior art, e.g. Coppola--Laporta (2015). Truncated trigonometric and indefinite moment problems have a large classical/operator-theoretic literature, including Derkach--Hassi--de Snoo (2012), and remain the appropriate context for WI-210--WI-212's finite-sample screening phenomena.

A fresh search around Dirichlet-kernel local limits, Gallagher short-interval mean squares, trigonometric moment interpolation, and indefinite moment completion did not locate a literature statement matching the specific lifted WI-211 bow-screen profile (1)--(3) or its exact source-coordinate dictionary (34)--(40). This absence is not used as a priority claim. The mathematical claim here is only that the displayed consequences follow exactly from the already-audited WI-211 screen plus classical identities.

## Research consequence

The `CLUE-two-harmonic-screen-continuum-residual` test is resolved in a narrowed form. Its central profile is correct; integer phase lifts reduce the best small-window coefficient by a factor `9` but cannot remove the residual; and the `1/M` frequency width is not a free synthetic channel but exactly a physical `XL/M` Gallagher-scale slab. The surviving bottleneck is therefore no longer the two-pair phase representative. It is the source-level complement: either prove a diagonal-scale bound for the full source-fixed error on this distinguished slab, or construct a more general off-line screen whose continuum residue cancels there as well.