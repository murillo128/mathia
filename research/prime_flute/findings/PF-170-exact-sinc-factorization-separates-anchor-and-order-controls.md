# PF-170 — exact sinc factorization separates anchor shift from gap-order controls

**Status:** `EXACT-DERIVED + LITERATURE-AUDITED + CONTROL/CALIBRATION`. PF-082 identified the first fixed-window projective defect of the exact endpoint law `V(x)=pi cot(pi/x)` at order `P^-4`, while PF-106 proved the much coarser all-span `O(P^-3)` tail equivalence with the exact all-composite shift clone `p_n -> p_n+1`. The present calculation gives an exact four-point factorization that sharpens both statements on consecutive finite blocks and answers the accepted gap-preserving-control clue. For three consecutive gaps, the exact canonical separator distinguishes the prime block from its affine all-composite clone only at **quintic** order, while a same-gap-multiset control that changes the middle gap is already visible in the projective tangent. Reversing only the two outer gaps is a finer control: it preserves the tangent and the complete quartic Schwarzian defect, and first appears at the same quintic order as the anchor shift.

The separation is intrinsic hyperbolic geometry — it is a primitive separator length and hence can also be realized as a marked/localized wave singularity time — but its anchor-sensitive coefficient comes from the universal cotangent endpoint law, not from primality. Thus finite-core separation from the shift clone exists, but it is not by itself an arithmetic selector.

## Claim

Let

\[
V(x)=\pi\cot\frac{\pi}{x},
\]

and take four increasing labels

\[
x_0=P,
\qquad
x_1=P+X,
\qquad
x_2=P+X+Y,
\qquad
x_3=P+H,
\qquad
H:=X+Y+Z,
\tag{1}
\]

with `X,Y,Z>0`. Define the exact PF-004 cross-ratio

\[
\chi_P(X,Y,Z)
:=
\frac{(V(x_2)-V(x_1))(V(x_3)-V(x_0))}
     {(V(x_1)-V(x_0))(V(x_3)-V(x_2))},
\tag{2}
\]

and its affine/projective tangent value

\[
\chi_0(X,Y,Z)
:=
\frac{YH}{XZ}.
\tag{3}
\]

For `0<=i<j<=3` put

\[
\delta_{ij}
:=
\pi\left(\frac1{x_i}-\frac1{x_j}\right)
=
\frac{\pi(x_j-x_i)}{x_ix_j},
\qquad
\operatorname{sinc}t:=\frac{\sin t}{t}.
\tag{4}
\]

Then there is an **exact identity**

\[
\boxed{
\frac{\chi_P(X,Y,Z)}{\chi_0(X,Y,Z)}
=
\frac{
\operatorname{sinc}(\delta_{12})
\operatorname{sinc}(\delta_{03})
}{
\operatorname{sinc}(\delta_{01})
\operatorname{sinc}(\delta_{23})
}.
}
\tag{5}
\]

Set

\[
D:=(X+Y)(Y+Z),
\qquad
M_P:=P(P+X)(P+X+Y)(P+H).
\tag{6}
\]

Whenever `H<=P/2`, the small-angle expansion of (5) is uniform and gives

\[
\boxed{
\log\frac{\chi_P}{\chi_0}
=
-\frac{\pi^2}{3}\frac{D}{M_P}
+O\!\left(\frac{H^4}{P^8}\right).
}
\tag{7}
\]

For four consecutive odd primes, write

\[
P=p_n,
\qquad
X=g_n,
\qquad
Y=g_{n+1},
\qquad
Z=g_{n+2}.
\tag{8}
\]

The Baker--Harman--Pintz short-interval bound recorded in S6 gives `H=O(P^0.525)`. The exact affine clone starts at `Q=P+1`; because `P` is odd and all three gaps are even, the four clone labels

\[
Q,
\quad Q+X,
\quad Q+X+Y,
\quad Q+H
\tag{9}
\]

are all even composites. Equations (7)--(9) imply

\[
\boxed{
\log\frac{\chi_{P+1}(X,Y,Z)}{\chi_P(X,Y,Z)}
=
\frac{\pi^2D}{3}
\left(\frac1{M_P}-\frac1{M_{P+1}}\right)
+O\!\left(\frac{H^4}{P^8}\right)
}
\tag{10}
\]

and therefore

\[
\boxed{
\log\frac{\chi_{P+1}}{\chi_P}
=
\frac{4\pi^2}{3}\frac{D}{P^5}
\left(1+O(P^{-0.475})\right)>0
}
\tag{11}
\]

for all sufficiently large consecutive-prime blocks. Since `D<=H^2`, this local shift defect is in particular `O(P^-3.95)`, much smaller than the all-span `O(P^-3)` envelope of PF-106.

Now compare two **all-composite** controls at the same even anchor `Q=P+1`: the ordered gap block `(X,Y,Z)` and the outer-reversed block `(Z,Y,X)`. They have the same tangent cross-ratio and the same quartic projective defect. More precisely,

\[
\boxed{
\log
\frac{\chi_Q(X,Y,Z)}{\chi_Q(Z,Y,X)}
=
\frac{\pi^2D}{3}
\frac{(X-Z)(2Q+H)}{
Q(Q+H)(Q+X)(Q+X+Y)(Q+Z)(Q+Z+Y)
}
+O\!\left(\frac{H^4}{Q^8}\right).
}
\tag{12}
\]

Hence, when `X!=Z`,

\[
\boxed{
\log
\frac{\chi_Q(X,Y,Z)}{\chi_Q(Z,Y,X)}
=
\frac{2\pi^2}{3}
\frac{D(X-Z)}{Q^5}
\left(1+O(P^{-0.475})\right).
}
\tag{13}
\]

The sign is eventually the sign of `X-Z`. If `X=Z`, the two ordered triples are identical and the difference vanishes exactly.

Finally, let `(A,M,B)` be any permutation of the same multiset `{X,Y,Z}` and keep the same even composite anchor `Q`. Its tangent value is

\[
\boxed{
\chi_0(A,M,B)
=
\frac{MH}{AB}
=
\frac{H M^2}{XYZ}.
}
\tag{14}
\]

Thus changing which gap occupies the middle position gives

\[
\boxed{
\log
\frac{\chi_Q(A,M,B)}{\chi_Q(X,Y,Z)}
=
2\log\frac{M}{Y}
+O\!\left(\frac{H^2}{Q^4}\right).
}
\tag{15}
\]

Equation (15) is the leading ordered-gap control. The special outer reversal keeps `M=Y`, so its tangent term cancels and the first orientation-sensitive contribution drops to the quintic scale (12)--(13).

## 1. Cotangent differences give the exact sinc factorization

For `x<y`, the elementary identity

\[
\cot b-\cot a
=
\frac{\sin(a-b)}{\sin a\sin b}
\]

with `a=pi/x`, `b=pi/y` gives

\[
V(y)-V(x)
=
\pi\frac{
\sin\left(\pi(1/x-1/y)\right)
}{
\sin(\pi/x)\sin(\pi/y)
}.
\tag{16}
\]

Insert (16) into the four differences of (2). Every individual `sin(pi/x_i)` occurs once in the numerator and once in the denominator, so all endpoint factors cancel exactly:

\[
\chi_P
=
\frac{
\sin\delta_{12}\sin\delta_{03}
}{
\sin\delta_{01}\sin\delta_{23}
}.
\tag{17}
\]

On the other hand,

\[
\frac{\delta_{12}\delta_{03}}
     {\delta_{01}\delta_{23}}
=
\frac{YH}{XZ}
=\chi_0,
\tag{18}
\]

because all four products `x_ix_j` cancel. Dividing (17) by (18) proves (5).

This exact identity is a stronger calibration than expanding the four endpoint values separately. It isolates the nonprojective part of the endpoint law into four elementary `sinc` factors; no off-prime interpolation is being promoted to geometry.

## 2. The quartic Schwarzian term has an exact rational carrier

For small `t`,

\[
\log\operatorname{sinc}t
=-\frac{t^2}{6}+O(t^4).
\tag{19}
\]

All four angles in (4) satisfy `|delta_ij|<=pi H/P^2`, so under `H<=P/2` the remainder in (19) is uniform. The decisive algebraic identity is

\[
\boxed{
\delta_{12}^2+
\delta_{03}^2-
\delta_{01}^2-
\delta_{23}^2
=
\frac{2\pi^2D}{M_P}.
}
\tag{20}
\]

It follows by substituting the four reciprocal differences and clearing the common denominator `M_P^2`; the numerator factors as

\[
2(X+Y)(Y+Z)M_P.
\]

Combining (5), (19), and (20) proves (7).

For fixed gaps, expanding `M_P^-1` recovers PF-082's Schwarzian coefficient

\[
\log\frac{\chi_P}{\chi_0}
=-\frac{\pi^2D}{3P^4}+O(P^{-5}).
\tag{21}
\]

The gain here is uniformity for the actual consecutive-prime window `H=O(P^0.525)`: the next error coming from `log sinc` is already `O(H^4/P^8)`, so the exact rational denominator carries all lower finite-scale corrections needed for the controls below.

## 3. The affine clone changes only the absolute anchor at quintic order

The normalized PF-106 affine clone uses `V(p+1)-1`. Translation by `-1` is Möbius and does not change cross-ratios, so on the block (8) its exact cross-ratio is simply `chi_(P+1)(X,Y,Z)`.

Subtracting (7) at `P` and `P+1` gives (10). Since

\[
\frac1{M_P}-\frac1{M_{P+1}}
=
\frac4{P^5}
\left(1+O\left(\frac{H+1}{P}\right)\right),
\tag{22}
\]

and S6 gives `H=O(P^0.525)`, the main term in (10) has the asymptotic form in (11). The `sinc` remainder is smaller: for even prime gaps `X,Y,Z>=2`, one has `D=(X+Y)(Y+Z)>=2H`, so

\[
\frac{H^4/P^8}{D/P^5}
\le
\frac{H^3}{2P^3}
=O(P^{-1.425}).
\tag{23}
\]

Thus the sign in (11) is not a numerical accident. On every sufficiently far four-consecutive-prime block, the exact separator of the shifted all-composite clone is slightly longer in cross-ratio coordinate than the prime separator, even though the full ordered gap sequence is identical.

This is exactly the kind of anchor-sensitive finite-core separation requested by `CLUE-gap-preserving-control-target-transport`, but it has a sharp evidence boundary: the coefficient is forced by the smooth universal endpoint law `V`, so the effect would occur for any labels translated through the same cotangent construction. The control proves **absolute-anchor sensitivity**, not sensitivity to the prime predicate.

## 4. Same-multiset controls separate two levels of order information

Because every odd-prime gap is even, starting at the even anchor `Q=P+1` and adding the gaps in **any order** produces only even composite labels. This gives exact same-multiset controls without a CRT construction or a probabilistic existence claim.

There are two qualitatively different reorderings.

First, moving a different gap into the middle position changes the affine/projective cross-ratio itself. Since the total `H` and product `XYZ` are unchanged, (14) follows immediately. Equation (7) for each ordering then gives (15). Thus this separator sees the identity of the **middle gap** at tangent order.

Second, swapping only the outer gaps leaves the middle gap, `H`, `XYZ`, and therefore `chi_0` unchanged. It also leaves

\[
D=(X+Y)(Y+Z)
\]

unchanged, so the complete quartic term in (7) cancels. The first surviving term comes from the fact that the rational carrier `M_Q` remembers which outer gap lies on the left. Indeed,

\[
\frac1{M_Q(X,Y,Z)}-
\frac1{M_Q(Z,Y,X)}
=
\frac{(Z-X)(2Q+H)}{
Q(Q+H)(Q+X)(Q+X+Y)(Q+Z)(Q+Z+Y)
},
\tag{24}
\]

which inserted into (7) proves (12). Under S6 the remainder is again lower order whenever `X!=Z`, giving (13).

So one scalar separator already exhibits a strict hierarchy:

\[
\boxed{
\begin{array}{rcl}
\text{middle-gap placement}
&:& \text{projective/tangent order},\\[2mm]
\text{outer left/right orientation}
&:& P^{-5}\text{ exact-circle order},\\[2mm]
\text{absolute anchor shift }P\mapsto P+1
&:& P^{-5}\text{ exact-circle order}.
\end{array}
}
\tag{25}
\]

The two quintic effects are different: the anchor shift has a universal positive coefficient proportional to `4D`, whereas outer orientation has a signed coefficient proportional to `2D(X-Z)`.

## 5. Hyperbolic length and localized spectral realization

PF-004 turns the cross-ratio into the primitive canonical separator length

\[
L(\chi)=4\operatorname{arsinh}\sqrt\chi.
\tag{26}
\]

Put

\[
L_0:=4\operatorname{arsinh}\sqrt{\chi_0}.
\]

Since

\[
\frac{dL}{d\log\chi}
=2\sqrt{\frac{\chi}{1+\chi}}
=2\tanh\frac{L}{4},
\tag{27}
\]

and (7) implies `chi_P/chi_0 ->1` uniformly on the BHP window, (11) yields

\[
\boxed{
L_{P+1}(X,Y,Z)-L_P(X,Y,Z)
=
\frac{8\pi^2}{3}
\frac{D}{P^5}
\tanh\frac{L_0}{4}
\left(1+O(P^{-0.475})\right)>0.
}
\tag{28}
\]

Likewise, for `X!=Z`,

\[
\boxed{
L_Q(X,Y,Z)-L_Q(Z,Y,X)
=
\frac{4\pi^2}{3}
\frac{D(X-Z)}{Q^5}
\tanh\frac{L_0}{4}
\left(1+O(P^{-0.475})\right).
}
\tag{29}
\]

These are intrinsic marked-length statements on the exact hyperbolic blocks, not arithmetic generating functions.

PF-064/PF-082 already supply the spectral realization needed for the clue's requested finite-core readout: after compact spatial/microlocal localization around an isolated primitive separator, the global prime-flute wave kernel has a nonzero singularity at the exact primitive length. Therefore (28)--(29) can be read as shifts of a **marked localized wave singularity time** whenever the same isolation/localization hypotheses are imposed. No new global trace formula, unmarked inverse theorem, or wave-operator statement is inferred.

## 6. What the control actually falsifies

PF-166/PF-168 show that broad moving-tail length and fixed-filter Dirichlet spectral data become asymptotically shift-clone blind. PF-170 shows why that does not mean every finite marked observable is literally equal on the two surfaces: exact-circle geometry retains an anchor-sensitive residue, and a primitive separator detects it.

But the residue is a universal projective-curvature effect. The source/shift comparison therefore supports only the following calibrated statement:

\[
\boxed{
\text{ordered gaps alone do not determine the exact finite block,}
\quad
\text{but the missing local datum is not automatically primality.}
}
\tag{30}
\]

The same-multiset controls sharpen this further. A change of middle gap probes projective ordered-gap shape before any anchor information enters. Outer reversal holds that tangent shape fixed and shows that exact-circle geometry contains a weaker orientation channel at the same quintic scale as the anchor shift. Any future mixed observable claiming arithmetic selectivity must therefore say which of these carriers it uses instead of treating “prime versus composite” as one undifferentiated target.

This resolves the local construction question in `CLUE-gap-preserving-control-target-transport`: a canonical nontrivial anchor-sensitive marked observable exists and its responses to the requested controls are explicit. What remains is a **different global question** already present in the line's current operator/nonlocal program: whether the vanishing universal finite-scale residues can be assembled into a canonical reference-stable global quantity whose organization is not reproduced by admissible composite controls.

## 7. Prior-art and novelty audit

No novelty is claimed for the cotangent subtraction identity (16), the Taylor series of `log(sin t/t)`, Schwarzian/cross-ratio distortion, hyperbolic translation length as a function of a four-point cross-ratio, or the Baker--Harman--Pintz exponent. PF-082 already audits the classical Schwarzian interpretation and its `P^-4` fixed-window consequence; S6 is the existing primary-source anchor for the only number-theoretic estimate imported here.

A directed external audit also recovered Alexey Teplinsky, *On cross-ratio distortion and Schwarz derivative*, Nonlinearity 21 (2008), 2777--2783, arXiv:0710.2629, DOI `10.1088/0951-7715/21/12/003`, which proves general asymptotic cross-ratio-distortion estimates in terms of the Schwarzian. That general theory is prior art and is **not** needed as a theorem in the derivation above.

Searches combining cotangent endpoint laws, prime gaps, cross-ratios, hyperbolic flutes, and all-composite controls did not locate the project-specific specialization (5), the rational carrier (20), or the three-way prime/shift/reorder calibration. Search absence is not a novelty proof. The durable contribution is the exact elementary factorization and its consequence for the already-canonical Mathia controls:

\[
\boxed{
\text{cotangent four-point geometry}
\longrightarrow
\text{exact sinc distortion}
\longrightarrow
\text{quartic tangent defect}
\longrightarrow
\text{quintic anchor/orientation split}.
}
\tag{31}
\]

## 8. Falsification core

A later adversary can audit PF-170 through a short finite chain:

1. verify the exact cotangent difference formula (16) and cancellation of all endpoint sine factors in the PF-004 cross-ratio;
2. divide by the reciprocal-angle cross-ratio to obtain the exact sinc identity (5);
3. check the rational algebra (20), independently of any asymptotic series;
4. use `log sinc t=-t^2/6+O(t^4)` and `|delta_ij|<=pi H/P^2` to obtain the uniform remainder in (7);
5. for consecutive primes, use only S6 to get `H=O(P^0.525)` and verify that the remainder is lower order than the shift term;
6. check that `P+1` plus any permutation of the three even prime gaps produces four even composite labels;
7. verify the exact denominator difference (24), which makes outer reversal invisible through quartic order but visible at quintic order when `X!=Z`;
8. differentiate (26) in logarithmic cross-ratio coordinate to obtain (28)--(29);
9. preserve the evidence boundary: the separator distinguishes exact finite blocks, but its anchor coefficient is generated by the universal endpoint law and does not certify primality or RH.

A failure of steps 1--4 would refute the core factorization/asymptotic claim. A failure of a later global accumulation mechanism would not refute PF-170; it would reinforce the conclusion that the local exact-circle residue is only a calibration channel.

## Research consequence

The accepted gap-preserving-control question no longer needs an unspecified “minimal anchor-sensitive observable.” The canonical separator itself, or its marked localized wave time, provides one. Its control response is now resolved at two scales: projective order carries which gap is central, while quintic exact-circle order carries both absolute anchor and the left/right orientation of the outer gaps.

This is useful mainly as a constraint. A future prime-flute spectral mechanism cannot claim primality specificity merely because it detects the `P^-5` source/shift difference; that difference is a universal cotangent-curvature effect. The remaining high-value target is genuinely global: an invariant must organize these vanishing local residues across the infinite flute in a way that survives reference/control audits and cannot be reproduced by the same admissible composite constructions.