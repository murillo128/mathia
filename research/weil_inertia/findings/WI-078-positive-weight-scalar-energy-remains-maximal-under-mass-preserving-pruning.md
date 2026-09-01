# WI-078 — Positive Yang scalar weights retain maximal additive-energy exponent under mass-preserving pruning

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE + PRIOR-ART-REDIRECTION`. This finding does **not** certify the Yang--Yang one-sided fourth-moment candidate and does not change Mathia's current unconditional simple-critical proportion. It sharpens the scalar-modulus obstruction chain WI-075--WI-077: even if the exact nonnegative Yang source weights are retained rather than collapsed to an unweighted support, their natural weighted symmetric and asymmetric additive energies already have the maximal exponent. Moreover, every pruning that retains a subpolynomial fraction of that positive source mass still has the same exponent.

The conclusion is deliberately sign-sensitive. It closes positive/absolute-weight scalar-energy and positive-mass-pruning escapes on the fixed source subfamily below. It does **not** close a scalar transform applied only after the centered signed combination `S1 - 2*S2 + S3` or after subtraction of the genuine four-form local main; cancellation in those signed coefficients remains a genuinely different information carrier.

## 1. The fixed `(5,7)` source slope supplies a positive measure of total mass `asymp X`

WI-076 works inside the same one-sided fixed-coefficient interior from WI-050 with

\[
(b_1,b_2)=(5,7),
\qquad
m'=m-5k,
\qquad
n'=n-7k,
\]

and defines the nonnegative slice weights

\[
W_k(X)
:=
\sum_{(m,n):(m,n,k)\in K^*_{5,7}(X)}
\Lambda(m)\Lambda(m-5k)\Lambda(n)\Lambda(n-7k).
\tag{1}
\]

The admissible positive `k` lie in one interval `I_X` of length `O(X)`. Bienvenu's established finite-complexity prime-pattern theorem, through the source-interface audit in WI-050/WI-076, gives

\[
\sum_{k\in I_X}W_k(X)
= c_{5,7}X^3(1+o(1))
\tag{2}
\]

for one source-dependent constant `c_{5,7}>0`. The elementary slice bound from WI-076 gives uniformly

\[
0\le W_k(X)\ll X^2(\log X)^4.
\tag{3}
\]

Normalize away the deterministic two-dimensional slice scale by

\[
u_k:=\frac{W_k(X)}{X^2}.
\tag{4}
\]

Then, writing

\[
U_X:=\sum_{k\in I_X}u_k,
\]

(2)--(3) become

\[
\boxed{
U_X\asymp X,
\qquad
0\le u_k\ll(\log X)^4,
\qquad
\operatorname{diam}(I_X)=O(X).
}
\tag{5}
\]

No new prime-pattern estimate is used below. Everything after (5) is a finite weighted-convolution argument.

## 2. The positive weighted symmetric energy is forced to exponent three

Define the weighted additive energy of the positive scalar measure `u` by

\[
\mathcal E^+(u)
:=
\sum_{a+b=c+d}u_au_bu_cu_d
=
\sum_s
\left(\sum_{a+b=s}u_au_b\right)^2.
\tag{6}
\]

Set

\[
r_u(s):=\sum_{a+b=s}u_au_b.
\]

Since `I_X+I_X` has `O(X)` integer values and

\[
\sum_s r_u(s)=U_X^2,
\]

Cauchy--Schwarz gives

\[
\mathcal E^+(u)
\ge
\frac{U_X^4}{|I_X+I_X|}
\gg X^3.
\tag{7}
\]

There is a matching exponent-level upper bound. In an additive quadruple, `a,b,c` determine `d`; hence, with `u_{\max}:=\max_k u_k`,

\[
\mathcal E^+(u)
\le
u_{\max}U_X^3
\ll
X^3(\log X)^4.
\tag{8}
\]

Therefore

\[
\boxed{
\mathcal E^+(u)=X^{3+o(1)}.
}
\tag{9}
\]

This is the maximal possible exponent at the natural normalization (5): a positive measure of total mass `X^{1+o(1)}` supported in an interval of length `X^{1+o(1)}` cannot have a weighted additive-energy exponent below three.

Equivalently, before normalization,

\[
\boxed{
\mathcal E^+(W)
=X^{11+o(1)}.
}
\tag{10}
\]

The factor `X^8` between (9) and (10) is exactly the fourth power of the slice normalization `X^2`.

## 3. The nonzero-shift weighted energy also has exponent three

For an integer translate `h`, define

\[
\mathcal E_h^+(u)
:=
\sum_{a+b=c+d+h}u_au_bu_cu_d,
\qquad
\mathcal E_*^+(u)
:=
\max_{h\ne0}\mathcal E_h^+(u).
\tag{11}
\]

Every ordered quadruple determines exactly one `h=a+b-c-d`, so

\[
\sum_h\mathcal E_h^+(u)=U_X^4\asymp X^4.
\tag{12}
\]

Only `O(X)` values of `h` are possible. The zero-shift contribution obeys (8), and therefore

\[
\mathcal E_0^+(u)
\ll X^3(\log X)^4
=o(X^4).
\tag{13}
\]

Thus the nonzero shifts carry `\asymp X^4` total mass across only `O(X)` translates, which forces

\[
\mathcal E_*^+(u)\gg X^3.
\tag{14}
\]

Conversely the same three-variables-determine-the-fourth argument gives, for every fixed `h`,

\[
\mathcal E_h^+(u)
\le u_{\max}U_X^3
\ll X^3(\log X)^4.
\tag{15}
\]

Hence

\[
\boxed{
\mathcal E_*^+(u)=X^{3+o(1)}.
}
\tag{16}
\]

So passing from the unweighted support energies of WI-077 to the exact **positive source weights** does not reveal a lower-energy exponent. Both weighted quantities remain maximally structured at power scale.

## 4. Positive-mass pruning cannot create a power-sparse or low-energy family

Let `B_X\subseteq I_X`, and suppose the retained positive source mass satisfies

\[
U_{B_X}:=\sum_{k\in B_X}u_k
\ge \eta_X U_X,
\qquad
\eta_X=X^{-o(1)}.
\tag{17}
\]

Thus the pruning is allowed to lose any polylogarithmic or more generally subpolynomial fraction, but not a fixed power of the positive source mass. From (5),

\[
U_{B_X}=X^{1-o(1)}.
\tag{18}
\]

Since every retained atom is at most `X^{o(1)}`, immediately

\[
\boxed{
|B_X|
\ge
\frac{U_{B_X}}{u_{\max}}
=X^{1-o(1)}.
}
\tag{19}
\]

Thus such a pruning cannot produce support of size `O(X^{1-\delta})` for any fixed `\delta>0`.

More strongly, repeat the weighted convolution argument with `u` restricted to `B_X`. Its sumset and translate range are still `O(X)`, so

\[
\mathcal E^+(u1_{B_X})
\ge
\frac{U_{B_X}^4}{O(X)}
=X^{3-o(1)}.
\tag{20}
\]

The zero-shift energy is at most

\[
u_{\max}U_{B_X}^3
=X^{3+o(1)},
\]

and is `o(U_{B_X}^4)` because `u_{\max}/U_{B_X}=X^{-1+o(1)}`. Summing over the `O(X)` available shifts as in (12)--(16) therefore also gives

\[
\boxed{
\mathcal E_*^+(u1_{B_X})=X^{3+o(1)}
}
\tag{21}
\]

at exponent level, together with the corresponding symmetric statement

\[
\boxed{
\mathcal E^+(u1_{B_X})=X^{3+o(1)}.
}
\tag{22}
\]

Consequently, **any pruning that actually lowers the positive scalar support or positive weighted-energy exponent by a fixed power must discard a power-sized fraction of the raw positive `(5,7)` source mass.** Merely identifying a favorable high-mass subfamily cannot evade WI-076/WI-077 at power scale.

## 5. Consequence for the scalar escape left open by WI-077

WI-077 deliberately left two scalar possibilities open: weighted cancellation and mass-preserving pruning. The present argument splits them sharply.

The following route is now closed at exponent level:

\[
\boxed{
\text{raw nonnegative Yang scalar weights}
\;\longrightarrow\;
\text{positive weighted additive energy or positive-mass pruning}
\;\longrightarrow\;
\text{fixed-power sparse-large-sieve gain}.
}
\tag{23}
\]

The obstruction already occurs inside the single fixed reduced-direction label `(5,7)`. Therefore merely retaining the direction label while applying a positive scalar-energy theorem separately to each label does not remove the fixed-slope obstruction. A labelled transform that uses additional phase orthogonality or directional cancellation is a different mechanism and remains outside (23).

What genuinely remains live is **signed centering before energy is taken**. The Yang covariance is not the positive `S1` measure (1): its load-bearing combination is `S1 - 2*S2 + S3`, and the current clue further requires subtracting the genuine full four-form local main. Those operations create signed coefficients. For a signed scalar sequence `c_k`, cancellation in

\[
\sum_{a+b=s}c_ac_b
\]

can be invisible to the positive measure `|c_k|` and to every argument above. Thus a successful scalar reduction must exploit that sign/correlation structure, or preserve a genuinely multidimensional/directional operator, rather than hope that the positive source weights themselves become sparse or low-energy after projection.

This is a useful narrowing of the accepted `CLUE-yang-locked-covariance-leading-scale`: the unresolved arithmetic information is now even more specifically in the **centered signed covariance/fiber structure**, not in a hidden sparse or low-energy positive scalar carrier.

## 6. Prior-art and novelty boundary

No novelty is claimed for weighted convolution identities, Cauchy--Schwarz, the inequality `\mathcal E^+(u)\le u_{\max}(\sum u)^3`, or the averaging argument over additive translates. These are elementary additive-combinatorial facts for a finite positive measure.

The theorem-level arithmetic input is inherited from the already-audited source chain:

- Pierre-Yves Bienvenu, **A higher-dimensional Siegel--Walfisz theorem**, *Acta Arithmetica* 179 (2017), 79--100, DOI `10.4064/aa8600-10-2016`, arXiv:1607.06625. WI-050/WI-076 verify the interface from Bienvenu's finite-complexity prime-pattern asymptotic to the exact fixed `(5,7)` Yang source interior.
- Roger C. Baker, Marc Munsch and Igor E. Shparlinski, **Additive energy and a large sieve inequality for sparse sequences**, *Mathematika* 68 (2022), 362--399, DOI `10.1112/mtk.12140`, arXiv:2103.12659. Their printed theorem uses the ordinary symmetric and asymmetric energies of a scalar modulus sequence; WI-077 already shows that those unweighted energies are maximal for the effective Yang scalar support. The present finding does **not** claim that BMS proves a weighted-modulus theorem. It uses weighted energy only to close the proposed positive-weight analogue at the information-interface level.

A bounded literature audit of additive-energy/large-sieve formulations located the established BMS scalar-energy framework but no theorem whose hypotheses would turn the exact positive Yang weights into a power gain despite (9) and (16). This is not a priority claim. The durable Mathia deduction is the source-specific combination of WI-076's positive fixed-slope mass with the elementary weighted-energy inequalities and the resulting pruning obstruction.

No `SOURCES.md` update is needed because both load-bearing external sources are already durable anchors for this line and no new external theorem is imported.

## 7. Falsification and remaining gates

1. **Positive fixed-slope mass.** Equations (2)--(5) require the WI-050/WI-076 source interior and Bienvenu interface. If that inherited asymptotic were invalid, the weighted-energy conclusion would have to be revisited.
2. **The sign boundary is essential.** The theorem concerns nonnegative `W_k` and prunings measured by their positive mass. It does not bound a sign-sensitive energy of the centered `S1 - 2*S2 + S3` coefficients.
3. **Mass retention is explicit.** A pruning that keeps only `X^{-\delta}` of the positive mass for some fixed `\delta>0` lies outside (17). Such a severe prune could be power-sparse, but a separate argument would then have to show why discarding almost all positive raw mass still retains the centered covariance relevant to the fourth-moment proof.
4. **Direction-sensitive transforms remain live.** Since the proof is scalar within one fixed label, it does not rule out an operator that keeps `(r,q)` and exploits directional Fourier phases, orthogonality, or cancellation unavailable to a scalar positive measure.
5. **Two-dimensional source-adapted large sieves remain live.** The finding does not touch a theorem acting directly on WI-071's linked two-shift incidence geometry before scalar projection.
6. **The Yang covariance clue remains unresolved.** Controlling the post-local-main power-coefficient fibers outside the WI-054 range still requires a signed/correlation estimate, a Yang-specific dispersion theorem, or another genuinely new arithmetic input.