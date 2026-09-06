# ANF-081 — two-level clipping closes the full real-multiplicity gate

**Status:** `EXACT-DERIVED + CENTRAL-NOTCH + ALL-FINITE-REAL-MULTISETS + UNBOUNDED-SUPPORT + UNBOUNDED-MULTIPLICITY + UNBOUNDED-VARIATION + STRICT-MONTGOMERY-TAYLOR-IMPROVEMENT`. `ANF-078` closes every fixed occupancy cap, `ANF-079` closes every fixed multiplicative-scale count, and `ANF-080` closes every fixed sorted-prefix variation cap. None of those statements by itself covers a single profile against arbitrary positive integer occupancies. The remaining loss can be removed by splitting every occupancy vector into its clipped `1/2` part and a high-occupancy remainder, then using the combinatorial affine surplus to force the only dangerous regime into a uniformly small neighborhood of the clipped class.

There exist central-notch parameters

\[
J_s=J_{\rm MT}-s\phi_\eta\ge0,
\qquad
F_s=\widehat J_s,
\]

and a number `q_s in (0,1)` such that **every finite real multiset**, with arbitrary support cardinality and arbitrary positive integer site multiplicities, satisfies

\[
\boxed{
\sigma\ge 2N-q_s^{-1}E_{F_s}(k;X),
}
\tag{1}
\]

while

\[
\boxed{
2-\frac{C(J_s)}{q_s}>2-C_{\rm MT}.
}
\tag{2}
\]

Thus the central-notch ray survives the entire scalar finite-real multiplicity problem with one fixed profile, one fixed amplitude and one fixed affine intercept `A=2`. The multiplicity-scale complexity left open by `ANF-080` is therefore a proof-method loss, not a genuine real-axis obstruction. Any remaining obstruction to the BGSST-style universal certificate must use genuinely non-real geometry, not merely a more complicated finite real multiplicity vector.

## 1. The only dangerous weighted configurations are almost entirely clipped to multiplicity two

Retain the notation of `ANF-079`--`ANF-080`:

\[
R:=R_{\rm MT}=\widehat J_{\rm MT}\ge0,
\qquad
\Phi_\eta:=\widehat\phi_\eta,
\]

and for a finite real multiset with distinct support sites `x_i` and positive integer occupancies `k_i`, put

\[
W:=\sum_i k_i^2,
\qquad
N:=\sum_i k_i,
\qquad
\sigma:=\#\{i:k_i=1\},
\]

\[
P:=W-2N+\sigma
=
\sum_{k_i\ge2}k_i(k_i-2)\ge0,
\tag{3}
\]

and

\[
E_R(k;X)=W(1+\nu),
\qquad
\nu\ge0.
\tag{4}
\]

The nonnegativity of `nu` uses the pointwise fact `R(t)>=0` already used in `ANF-079` and `ANF-080`.

Now clip the occupancies at two:

\[
\ell_i:=\min(k_i,2),
\qquad
h_i:=(k_i-2)_+,
\qquad
k=\ell+h.
\tag{5}
\]

Write

\[
W_\ell:=\sum_i\ell_i^2,
\qquad
W_h:=\sum_i h_i^2.
\]

For every integer `k>=3`,

\[
(k-2)^2\le k(k-2),
\]

and

\[
k^2-4=(k-2)(k+2)\le2k(k-2).
\]

After summing sitewise,

\[
\boxed{
W_h\le P,
\qquad
W_\ell\ge W-2P.
}
\tag{6}
\]

Because `R>=0` pointwise and `0<=h_i<=k_i`, the off-diagonal Montgomery--Taylor energy of `h` is no larger than that of `k`. Hence

\[
\boxed{
E_R(h;X)
\le P+\nu W.
}
\tag{7}
\]

Similarly, if

\[
E_R(\ell;X)=W_\ell(1+\nu_\ell),
\]

then

\[
\boxed{
\nu_\ell W_\ell\le\nu W.
}
\tag{8}
\]

The point of (6)--(8) is that the affine surplus `P` is not merely a counting correction. It quantitatively controls the entire squared mass of the high-occupancy remainder. Therefore a configuration with both small Montgomery--Taylor excess and small affine surplus is forced close, in the exact quadratic sense needed below, to a vector taking only the values `1` and `2`.

## 2. The clipped vector has a universal notch-energy bound

The sorted-prefix variation of every `1/2` occupancy vector is at most

\[
\boxed{
\mathcal V(\ell)\le\frac43.
}
\tag{9}
\]

Indeed, a mixed vector has only the relative drop `2 -> 1`, contributing `1/3`, and the terminal drop `1 -> 0`, contributing `1`; a uniform `1` or `2` vector has variation `1`.

Retain from `ANF-080`

\[
B_{\eta,L}
:=
\frac4{c_0}\left(\eta+\frac4L\right),
\qquad
a_L=1+\frac2{\kappa_L},
\]

and

\[
p_L:=\sqrt{2\sqrt{a_L}},
\qquad
q_L:=\sqrt{2\sqrt{a_L}+a_L}.
\]

Its weighted notch estimate says

\[
\frac{E_{\Phi_\eta}(u;X)}{\sum_i u_i^2}
\le
\mathcal V(u)
\left(
\sqrt{b_\eta B_{\eta,L}}
+p_L\nu_u^{1/4}
+q_L\nu_u^{1/2}
\right)^2.
\tag{10}
\]

Fix `eta,L` for the moment. For `0<s<=1/8` define

\[
\boxed{
M_s
:=
\frac43
\left(
\sqrt{b_\eta B_{\eta,L}}
+p_L(4s)^{1/4}
+q_L(4s)^{1/2}
\right)^2
}
\tag{11}
\]

and

\[
\boxed{
G_s
:=
\left(\sqrt{M_s}+\sqrt{2s}\right)^2.
}
\tag{12}
\]

Suppose now that

\[
\boxed{
\frac PW+\nu<2s.
}
\tag{13}
\]

Then (6) and `s<=1/8` give

\[
W_\ell>(1-4s)W\ge\frac W2,
\]

so (8) yields

\[
\nu_\ell<4s.
\tag{14}
\]

Equations (9)--(11) therefore imply

\[
\boxed{
E_{\Phi_\eta}(\ell;X)\le M_sW.
}
\tag{15}
\]

The remainder is even cheaper. Since `0<=phi_eta<=J_MT`, the spectral quadratic forms are ordered:

\[
E_{\Phi_\eta}(h;X)\le E_R(h;X).
\]

Using (7) and (13),

\[
\boxed{
E_{\Phi_\eta}(h;X)<2sW.
}
\tag{16}
\]

Finally, `phi_eta>=0`, so `E_{Phi_eta}` is a squared Hilbert norm. Cauchy--Schwarz for the cross term between `ell` and `h` gives

\[
\begin{aligned}
E_{\Phi_\eta}(k;X)
&\le
\left(
\sqrt{E_{\Phi_\eta}(\ell;X)}
+
\sqrt{E_{\Phi_\eta}(h;X)}
\right)^2\\
&\le
\boxed{G_sW.}
\end{aligned}
\tag{17}
\]

Thus all unbounded multiplicity complexity disappears in the only regime where the affine surplus and the original Montgomery--Taylor excess are simultaneously too small to pay for a crude perturbative estimate.

## 3. A two-regime splice gives one affine certificate for every real multiset

Choose `eta,L` so that

\[
\boxed{
\frac43 C_{\rm MT}B_{\eta,L}
<
1+\frac{\eta^2}{3}.
}
\tag{18}
\]

This is possible because `B_{eta,L}` can be made arbitrarily small by taking `eta` small and then `L` large, exactly as in `ANF-034`. Keep this pair fixed. Since

\[
G_s\longrightarrow\frac43b_\eta B_{\eta,L}
\qquad(s\downarrow0),
\tag{19}
\]

(18) permits a sufficiently small positive `s` for which, in addition to `s<=1/8`,

\[
\boxed{
G_s<1,
\qquad
G_s<
\frac{b_\eta}{C_{\rm MT}}
\left(1+\frac{\eta^2}{3}\right).
}
\tag{20}
\]

Define

\[
\boxed{
d_s:=sG_s,
\qquad
q_s:=1-d_s,
\qquad
t_s:=q_s^{-1}.}
\tag{21}
\]

Because `G_s<1`,

\[
0<d_s<s,
\qquad
q_s>1-s>0.
\tag{22}
\]

Consider the affine slack

\[
\mathcal S
:=
\sigma-2N+t_sE_{F_s}(k;X).
\tag{23}
\]

Multiplying by `q_s` and using (3),

\[
q_s\mathcal S
=q_s(P-W)+E_{F_s}(k;X).
\tag{24}
\]

There are only two cases.

### Small-surplus/small-excess regime

If (13) holds, then (4) and (17) give

\[
\begin{aligned}
E_{F_s}(k;X)
&=E_R(k;X)-sE_{\Phi_\eta}(k;X)\\
&\ge
\left(1+\nu-sG_s\right)W\\
&=
(q_s+\nu)W.
\end{aligned}
\tag{25}
\]

Substitution into (24) yields the exact nonnegative lower bound

\[
\boxed{
q_s\mathcal S
\ge
q_sP+\nu W
\ge0.
}
\tag{26}
\]

### Complementary regime

If instead

\[
\frac PW+\nu\ge2s,
\tag{27}
\]

use only the spectral domination `phi_eta<=J_MT`:

\[
J_s=J_{\rm MT}-s\phi_\eta
\ge(1-s)J_{\rm MT}.
\]

Hence

\[
E_{F_s}(k;X)
\ge
(1-s)E_R(k;X)
=(1-s)(1+\nu)W.
\tag{28}
\]

Since `q_s>1-s`, equations (24), (27), and (28) give

\[
\begin{aligned}
\frac{q_s\mathcal S}{W}
&\ge
q_s\frac PW+d_s-s+(1-s)\nu\\
&\ge
 d_s-s+(1-s)\left(\frac PW+\nu\right)\\
&\ge
 d_s+s-2s^2
>0.
\end{aligned}
\tag{29}
\]

Thus (1) holds for **every** finite real multiset, with no restriction on support, maximum occupancy, occupied multiplicity scales, sorted-prefix variation, or geometry.

The splice is the essential step missing from `ANF-080`. Large multiplicity complexity cannot be dangerous by itself: if it creates appreciable integer surplus `P`, that surplus pays for the crude spectral loss. If it does not, clipping shows that almost all quadratic mass already lies in the bounded-variation `1/2` class where the refined near-face estimate is uniform.

## 4. The same normalization still beats Montgomery--Taylor

The central-notch cost is exact:

\[
C(J_s)
=
C_{\rm MT}
-sb_\eta\left(1+\frac{\eta^2}{3}\right).
\tag{30}
\]

By (20)--(21),

\[
d_s=sG_s
<
\frac{s b_\eta}{C_{\rm MT}}
\left(1+\frac{\eta^2}{3}\right).
\tag{31}
\]

Therefore

\[
C(J_s)
<
C_{\rm MT}(1-d_s)
=C_{\rm MT}q_s,
\]

or equivalently

\[
\boxed{
\frac{C(J_s)}{q_s}<C_{\rm MT}.
}
\tag{32}
\]

This proves the strict objective improvement (2). The parameter order is important: first choose a narrow notch width `eta` and large deletion scale `L` satisfying (18), then take the notch amplitude `s` sufficiently small to satisfy (20). No parameter depends on the eventual support size or multiplicity vector.

## 5. Adversarial audit and evidence boundary

The proof has seven load-bearing checks.

1. The clipping inequalities (6) are sitewise integer inequalities. They do not assume a bound on `max k_i`.
2. Equations (7)--(8) use the pointwise nonnegativity `R_MT>=0`, not positive definiteness alone.
3. The comparison `E_{Phi_eta}(h)<=E_R(h)` uses the spectral inequality `0<=phi_eta<=J_MT`; it is valid for arbitrary real coefficients and therefore for the remainder `h`.
4. The only imported weighted estimate is `ANF-080` equation (29), applied to `ell`. Its variation is universally at most `4/3`, and its Montgomery--Taylor excess is controlled by (8).
5. The cross term in (17) is controlled in `L^2(phi_eta d alpha)`, where positivity of `phi_eta` makes Cauchy--Schwarz exact and independent of the sign of the spatial transform.
6. The large-regime estimate (28) is a spectral order statement `J_s>=(1-s)J_MT`; it does not reuse the small-regime bound or assume small Montgomery--Taylor excess.
7. The objective comparison uses the exact cost (30). The strict margin in (18) survives as `s->0`, so the normalization payment `d_s=sG_s` is genuinely smaller than the spectral gain.

Several plausible failure modes were checked explicitly. A single enormous occupancy falls in the large-surplus regime because `P/W` is bounded away from zero. A huge cloud of `1/2` sites stays in the clipped regime and is already covered by the fixed `4/3` variation bound. A sparse collection of high occupancies hidden among many singletons has small high-part `L^2` mass by (6), while any attempt to make its interactions large is charged to `nu` through (7). Thus none of the three extreme ways of sending multiplicity complexity to infinity escapes the two-regime dichotomy.

The literature ingredients remain classical. Positive-definite/Fourier quadratic forms and Hilbert-space Cauchy--Schwarz are standard, and the neighboring statistical-mechanics literature already anchored in `SOURCES.md` (Sütő for nonnegative compact Fourier support and Procacci for stability language) covers the general occupation-energy setting. A targeted search for weighted positive-type pair energies, superstability occupation bounds, and truncation/clipping arguments did not identify a theorem that supplies the Mathia-specific affine splice (24)--(32). No novelty is claimed for positive-definite kernels, Fourier order, clipping, or Cauchy--Schwarz, and no new load-bearing literature source is needed.

This finding does **not** prove the full conjugation-invariant complex certificate, improve the unconditional zeta-zero proportion by itself, or imply RH. It closes the finite-real scalar multiplicity frontier for the central-notch shape family. The next obstruction must therefore exploit non-real points — in particular multi-pair geometry or a higher-order carrier — rather than unbounded support or unbounded integer occupancy on the real axis.