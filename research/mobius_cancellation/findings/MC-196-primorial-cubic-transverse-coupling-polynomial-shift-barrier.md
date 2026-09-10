# MC-196 — Primorial cubic transverse coupling lands in the rough zero mode but opens a polynomial-shift correlation barrier

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `FRONTIER-REFINEMENT`, `BOUNDARY/CONDITIONAL-GAIN`, `NEGATIVE/OBSTRUCTION`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

`MC-190` and `MC-194` show that unit-equivariant linear and Hermitian-quadratic statistics of the logarithmic-primorial residue vector cannot couple the principal rough Möbius mode to transverse character modes. `MC-195` then shows that the most canonical cubic additive triad of the raw one-dimensional prefix is already Mertens-complete. There is nevertheless a genuinely different cubic operation available **after residue aggregation**: products of nonprincipal character sectors can multiply back into the principal representation.

For the active logarithmic primorial

\[
q=q_y=\prod_{p\le y}p,
\qquad y=c\log X,
\qquad 0<c<\tfrac12,
\tag{1}
\]

put

\[
G=(\mathbb Z/q\mathbb Z)^\times,
\qquad \phi=|G|=\varphi(q),
\tag{2}
\]

and use the rough coefficient

\[
g(n)=\mu(n)\mathbf 1_{(n,q)=1}.
\tag{3}
\]

At this primorial, `(3)` is exactly the logarithmically rough Möbius coefficient of `MC-180`. For each reduced residue class define

\[
A_a=\sum_{\substack{n\le X\\n\equiv a\pmod q}}g(n),
\qquad
B_a=\sum_{\substack{n\le X\\n\equiv a\pmod q}}g(n)^2,
\qquad a\in G.
\tag{4}
\]

Write

\[
S=\sum_{a\in G}A_a=G_y(X),
\qquad
Q=\sum_{a\in G}B_a,
\tag{5}
\]

and center the two residue vectors:

\[
u_a=A_a-\frac S\phi,
\qquad
v_a=B_a-\frac Q\phi.
\tag{6}
\]

Define the purely transverse cubic statistic

\[
\boxed{
J_3:=\sum_{a\in G}u_a^3-3\sum_{a\in G}u_av_a.
}
\tag{7}
\]

Although `(6)` displays the centering using `S`, `J_3` does **not** require the principal Fourier coefficient as input: with normalized multiplicative Fourier coefficients

\[
\widehat A(\chi)=\frac1\phi\sum_{a\in G}A_a\overline{\chi(a)},
\qquad
\widehat B(\chi)=\frac1\phi\sum_{a\in G}B_a\overline{\chi(a)},
\tag{8}
\]

one has the exact nonprincipal representation

\[
\boxed{
\frac{J_3}{\phi}
=
\sum_{\substack{\chi_1\chi_2\chi_3=1\\\chi_1,\chi_2,\chi_3\ne1}}
\widehat A(\chi_1)\widehat A(\chi_2)\widehat A(\chi_3)
-3\sum_{\chi\ne1}\widehat A(\chi)\widehat B(\chi^{-1}).
}
\tag{9}
\]

Thus cubic representation products really do evade the quadratic sector-separation theorem: three nonprincipal characters can have product `1`.

The source arithmetic, however, forces an exact compensating term. Let

\[
P_2
:=
\sum_{a\in G}
\sum_{\substack{n_1,n_2\le X\\n_1\ne n_2\\n_1\equiv n_2\equiv a\pmod q}}
g(n_1)g(n_2)
\tag{10}
\]

be the ordered distinct same-residue pair correlation and

\[
D_3
:=
\sum_{a\in G}
\sum_{\substack{n_1,n_2,n_3\le X\\\text{pairwise distinct}\\n_1\equiv n_2\equiv n_3\equiv a\pmod q}}
g(n_1)g(n_2)g(n_3)
\tag{11}
\]

the ordered distinct same-residue cubic correlation. Then

\[
\boxed{
D_3-J_3
=
S\left(
2+\frac{3P_2}{\phi}-2\frac{S^2}{\phi^2}
\right).
}
\tag{12}
\]

Equivalently, if

\[
E_2:=\sum_{a\in G}u_a^2,
\tag{13}
\]

then

\[
\boxed{
D_3-J_3
=
S\left(
2+\frac{3(E_2-Q)}{\phi}+\frac{S^2}{\phi^2}
\right).
}
\tag{14}
\]

Equations `(12)`--`(14)` give the first exact source-level answer to the nonlinear escape left by `MC-190`/`MC-194`: **nonprincipal cubic sectors can land in the rough principal mode, but only together with off-diagonal same-residue correlations of the underlying Möbius coefficients.** The coupling is therefore real rather than representation-theoretically forbidden, yet it is not a free decoder for `S`.

At the active primorial scale the new source terms are polynomial-shift objects. Since equal reduced residues differ by multiples of `q`, define

\[
C_2(r)=\sum_{n\le X-r}g(n)g(n+r)
\tag{15}
\]

and

\[
C_3(r,s)=\sum_{n\le X-\max(r,s)}g(n)g(n+r)g(n+s).
\tag{16}
\]

Then, exactly,

\[
\boxed{
P_2=2\sum_{1\le h\le (X-1)/q} C_2(hq),
}
\tag{17}
\]

and

\[
\boxed{
D_3=6\sum_{1\le h<k\le (X-1)/q} C_3(hq,kq).
}
\tag{18}
\]

Because `q=X^{c+o(1)}` by the prime number theorem, the **first nonzero shift is already `X^{c+o(1)}`**, and the required pair/triple families live on the deterministic polynomially sparse lattice `q\mathbb N` and `(q\mathbb N)^2`. Existing logarithmic or almost-all Chowla information does not automatically control this prescribed lattice at fixed-power strength.

A generic moment restriction makes the sparsity loss explicit. If a family of correlations satisfies for some fixed `p>=1`

\[
\left(\frac1R\sum_{1\le r\le R}|C(r)|^p\right)^{1/p}
\le XE(X),
\tag{19}
\]

and `L=\lfloor R/q\rfloor`, then Hölder gives only

\[
\boxed{
\frac1L\sum_{1\le h\le L}|C(hq)|
\le
q^{1/p+o(1)}XE(X).
}
\tag{20}
\]

For `q=X^{c+o(1)}` and any fixed `p`, a merely logarithmic saving `E(X)=\log^{-A}X` is overwhelmed by the polynomial restriction cost `q^{1/p}`. For `p=1`, even the full averaged absolute correlation estimate can place essentially all of its allowed mass on the prescribed multiples of `q`. A theorem whose exceptional-shift density is only logarithmically small or `o(1)` has the same structural problem: the target shift lattice itself has density `X^{-c+o(1)}`.

Accordingly, the cubic escape is **mathematically genuine but source-expensive**. To turn `(12)` or `(14)` into a fixed-power bound for `S`, one needs new quantitative information on the same-residue pair/triple terms, or a different source identity in which those terms cancel or are controlled at polynomial strength. Current transverse dispersion alone does not provide that information.

## 1. Exact ternary algebra behind the coupling

Fix one residue class and abbreviate its nonzero/zero Möbius values by `x_i in {-1,0,1}`. Put

\[
A=\sum_i x_i,
\qquad
B=\sum_i x_i^2.
\]

Expanding `A^3`, the terms with all three indices equal contribute `A` because `x_i^3=x_i`. The terms with exactly two equal indices contribute

\[
3\sum_{i\ne j}x_i^2x_j
=3(BA-A).
\]

The remaining terms are precisely the ordered pairwise-distinct triple sum. Therefore

\[
\boxed{D_{3,a}=A_a^3-3B_aA_a+2A_a.}
\tag{21}
\]

Likewise the ordered distinct pair sum in one class is

\[
P_{2,a}=A_a^2-B_a.
\tag{22}
\]

Summing `(21)` over residue classes and inserting

\[
A_a=\frac S\phi+u_a,
\qquad
B_a=\frac Q\phi+v_a,
\qquad
\sum_a u_a=\sum_a v_a=0,
\tag{23}
\]

gives

\[
D_3
=
\frac{S^3}{\phi^2}
+\frac{3S}{\phi}E_2
-\frac{3QS}{\phi}
+2S
+J_3,
\tag{24}
\]

which is `(14)`. From `(22)`,

\[
P_2=E_2+\frac{S^2}{\phi}-Q,
\tag{25}
\]

and substitution yields `(12)`.

No analytic continuation, zero-free region, probabilistic independence, or estimate for `M` enters this derivation. The only source-specific algebra is the ternary identity `g^3=g` and the residue partition.

## 2. Why `J_3` is genuinely transverse

The centering in `(6)` removes exactly the principal character. Fourier inversion gives

\[
u_a=\sum_{\chi\ne1}\widehat A(\chi)\chi(a),
\qquad
v_a=\sum_{\chi\ne1}\widehat B(\chi)\chi(a).
\tag{26}
\]

Summing products over `a` and using character orthogonality proves `(9)`. In particular, the cubic term survives precisely when three nonprincipal characters multiply to the trivial character. This is the representation-product mechanism that is absent at linear level and absent from Hermitian quadratic forms diagonalized in `MC-190`/`MC-194`.

The second term of `J_3` is not an arbitrary correction chosen to manufacture `(12)`. It is forced by the exact ternary source relation `(21)`: `B_a` records the square-free rough support needed to subtract repeated-index contributions from the cube of a signed class sum.

This also separates the present statistic from `MC-195`. There the cubic convolution of the raw prefix collapses because pointwise Möbius nonlinearity on `{-1,0,1}` has only the basis `1,mu,mu^2`. Here the nonlinearity is applied **after many coefficients have been aggregated into residue-class sums**, so `A_a` is not ternary and the cubic transverse character product is a genuinely different operation. The price is exactly the multi-point source correlation in `(11)`.

## 3. The polynomial-shift lattice is the new arithmetic burden

For a pair of distinct integers in the same class modulo `q`, their difference is `hq` for a unique nonzero integer `h`; symmetry of the ordered pair gives `(17)`. For a triple, choose its smallest member `n` and write the other two as `n+hq` and `n+kq` with `1<=h<k`. Every unordered triple has `3!` ordered permutations and the product is symmetric, giving `(18)`.

At `y=c log X`, the PNT estimate

\[
\log q=\vartheta(y)=y+o(y)
\]

gives

\[
q=X^{c+o(1)}.
\tag{27}
\]

Thus these are not fixed-shift Chowla correlations and not polylogarithmic growing shifts. They are correlations on a prescribed lattice whose spacing is itself a fixed power of `X`. Moreover `g(n)=mu(n)1_{(n,q)=1}` is a scale-dependent pre-sieved coefficient, so transferring an ordinary Möbius correlation theorem to `(15)`--`(16)` requires an additional sieve-weight audit rather than a silent substitution.

The sparse-restriction inequality `(20)` is elementary. Hölder gives

\[
\sum_{h\le L}|C(hq)|
\le
L^{1-1/p}\left(\sum_{r\le R}|C(r)|^p\right)^{1/p},
\]

and `R/L=q^{1+o(1)}` gives `(20)`. The estimate is intentionally information-theoretic: a theorem may beat it only by using arithmetic structure that distinguishes the multiples of the primorial from a generic sparse subset.

## 4. Audit against current correlation and higher-uniformity prior art

The averaged Chowla theorem `MC-S13`, already audited in `MC-006`, gives quantitative decay after averaging absolute two-point correlations over a full interval of shifts, with logarithmic rather than fixed-power strength. The present target is a deterministic polynomially sparse subfamily of those shifts. The theorem statement by itself does not prevent its allowed correlation mass from concentrating on the multiples of `q`; `(20)` quantifies the generic restriction loss.

Guo's recent quantitative logarithmic Chowla preprint `MC-S29`, audited in `MC-041`, strengthens harmonic two-point control and includes growing shifts. Its uniformly controlled individual shift range is polylogarithmic, while the first primorial shift here is `X^{c+o(1)}`. Its polynomial shift-window result is an averaged fixed-`p` statement for logarithmically weighted **Liouville** correlations; even before the Möbius/pre-sieving mismatch, restricting such a log-strength moment bound to `q\mathbb N` pays the `q^{1/p}` factor in `(20)` and does not create fixed-power cancellation.

The 2026 Matomäki--Radziwiłł--Shao--Tao--Teräväinen higher-uniformity theorem `MC-S2` gives very strong almost-all short-interval Möbius/nilsequence control, and in the range `H>=X^{1/3+epsilon}` quantitative inverse-logarithmic savings with inverse-logarithmic exceptional measure. As already quantified in `MC-001`, that currency is insufficient for a black-box fixed-power local-to-global transfer. It also does not state the predetermined two-parameter polynomial-shift estimate `(18)`. The paper explicitly treats its Gowers-uniformity conclusions as qualitative in the broader power-window regime and notes that substantially better range/quantification would be needed for logarithmic Chowla applications.

No claim is made that the methods inside these papers are incapable of reaching `(17)`--`(18)`. The conclusion is narrower: **their currently stated theorem outputs do not pay the exact polynomially sparse, pre-sieved pair/triple correlation budget exposed by the cubic residue identity.**

The algebra `(21)` and finite-group Fourier expansion `(9)` are elementary and are not claimed as new general theorems. A targeted literature search over Möbius higher correlations, moments in arithmetic progressions, and higher-uniformity/averaged-Chowla results found the established component languages but no source that supplies the specific fixed-power primorial-lattice estimates needed here. The durable Mathia delta is therefore the exact composition boundary relative to the live `MC-180` rough decomposition and the `MC-190`--`MC-195` representation no-go chain.

## 5. Boundaries and falsification tests

- Equation `(12)` is an exact constraint, **not** a reconstruction theorem for `S`. The bracket can in principle be small or change sign, so stable inversion requires an independently proved conditioning statement.
- `J_3` is transverse in character space, but no current theorem in the line gives the fixed-power bound on `J_3` that a successful argument would need. Cubic products can amplify transverse coefficients even when a quadratic dispersion estimate is available.
- `D_3` and `P_2` are not errors that may be dropped. They are the exact repeated-class source correlations forced when the aggregate cube is expanded.
- The shift identities `(17)`--`(18)` concern the pre-sieved coefficient `g`, not unrestricted `mu`; an ordinary Chowla estimate cannot be inserted without proving the transfer through `1_{(n,q)=1}`.
- The sparse-lattice obstruction `(20)` applies to black-box fixed-`p` moment information. A theorem specifically uniform on primorial multiples, a signed identity coupling those shifts, or moment control with quantitatively growing `p` and usable constants could evade it.
- No independence or random-multiplicative heuristic is used to assert that `E_2` is close to `Q`. Such a statement would be an additional theorem, not a consequence of centering.
- Nothing here improves the unconditional bound for `G_y(X)` in `MC-187`, the ordinary Mertens function, or the zero-free region of `zeta`.

A continuation of this nonlinear route becomes substantive only if it proves one of the missing source statements at polynomial strength: a conditioned version of `(12)`/`(14)`, a fixed-power estimate for the primorial-lattice pair/triple correlations, or a different nonlinear source relation in which the collision terms cancel before absolute values are taken. Conversely, a matched multiplicative control that reproduces the available transverse statistics and low-order collision bounds while allowing a large principal sum would kill the proposed information class.

## Consequence for the active frontier

The sequence `MC-188`--`MC-194` did not merely fail to find a principal/transverse coupling; it proved that the natural equivariant linear/quadratic and additive-shell categories cannot contain one. `MC-195` then showed that a raw cubic additive triad is target-complete rather than intermediate.

The present finding sharpens the remaining nonlinear escape. **Cubic residue aggregation really can couple nonprincipal sectors into the principal representation without inserting the principal coefficient into the transverse statistic.** But the source identity immediately converts that apparent representation-theoretic gain into pair and triple Möbius correlations on a polynomially spaced primorial lattice. Current Chowla/higher-uniformity outputs live in the wrong quantitative or shift-uniformity class for that burden.

The next useful attack should therefore be source-side rather than another change of Fourier basis: either find arithmetic structure special to the primorial multiples in `(17)`--`(18)` that gives polynomial cancellation, or show that every natural low-degree nonlinear aggregate produces an analogous collision hierarchy. The latter would turn the present cubic calculation into a broader no-go for finite-degree nonlinear post-aggregation routes.