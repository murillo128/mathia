# MC-365 — Coordinatewise binary-symmetric channels asymptotically saturate the endpoint information, Hellinger, and log-affinity tariffs

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-361`--`MC-364` progressively sharpen the reciprocal endpoint admission cost from mutual information to Hellinger edge mass and finally to additive negative log-affinity for source-independent product channels. Those lower bounds are not only qualitatively natural: at the abstract channel level their endpoint constants and their small-error scaling are already asymptotically sharp.

Continue the punctured-cube source notation

\[
\Xi=\mathbf F_2^R\setminus\{0\},
\qquad
m=2^R-1,
\qquad
q_R=\frac{m-1}{m},
\]

with the associated source phases

\[
X=(X_1,\ldots,X_R)\in\{-1,+1\}^R
\]

and `X` uniform on the corresponding punctured cube. Fix

\[
0\le \delta\le\frac12
\]

and pass each coordinate independently through a binary-symmetric channel:

\[
Y_i=X_i Z_i,
\qquad
\mathbf P(Z_i=-1)=\delta,
\qquad
\mathbf P(Z_i=+1)=1-\delta,
\]

with the `Z_i` independent of one another and of `X`.

For two surviving source states `x,x'` differing in exactly one coordinate, their transcript laws satisfy

\[
\boxed{
\operatorname{Aff}(P_x,P_{x'})
=2\sqrt{\delta(1-\delta)},
}
\tag{1}
\]

and hence

\[
\boxed{
H^2(P_x,P_{x'})
=1-2\sqrt{\delta(1-\delta)}.
}
\tag{2}
\]

Writing

\[
\lambda_\delta
:=-\log\!\left(2\sqrt{\delta(1-\delta)}\right),
\tag{3}
\]

the source-independent product architecture with one component `Y_i` per source coordinate has exactly

\[
\Lambda_i=\lambda_\delta
\qquad(1\le i\le R).
\tag{4}
\]

Thus the product-affinity inequality underlying `MC-364` is an equality on every surviving cube edge.

The same binary channel also saturates the sharp Jensen--Shannon/Hellinger envelope used in `MC-363`. Indeed

\[
\boxed{
\operatorname{JS}(P_x,P_{x'})
=\log2-h(\delta)
=\Phi\!\left(1-2\sqrt{\delta(1-\delta)}\right),
}
\tag{5}
\]

where `h` and `Phi` are the functions of `MC-363`. Since every surviving edge has the same Hellinger cost, the concavity/Jensen step in that finding also has no dispersion loss.

The puncture removes exactly one edge in each coordinate direction. Hence each direction retains `(m-1)/2` undirected edges and the normalized Hellinger edge mass is exactly

\[
\boxed{
\frac{\mathfrak H_1}{R}
=q_R\left(1-2\sqrt{\delta(1-\delta)}\right).
}
\tag{6}
\]

Finally, the mutual-information floor of `MC-361` is asymptotically attained as well. Since the product BSC has

\[
H(Y\mid X)=Rh(\delta),
\tag{7}
\]

while adding independent group noise cannot decrease entropy,

\[
H(Y)\ge H(X)=\log m,
\tag{8}
\]

and the binary output alphabet gives

\[
H(Y)\le R\log2.
\tag{9}
\]

Therefore

\[
\boxed{
\log m-Rh(\delta)
\le I(X;Y)
\le R\log2-Rh(\delta),
}
\tag{10}
\]

so the gap from the `MC-361` binary-entropy lower floor is bounded by

\[
0\le
I(X;Y)-[\log m-Rh(\delta)]
\le
\log\frac{2^R}{2^R-1}
=O(2^{-R}).
\tag{11}
\]

Now set

\[
\delta=\frac\varepsilon2.
\tag{12}
\]

Then the BSC has

\[
1-2\sqrt{\delta(1-\delta)}
=1-\sqrt{2\varepsilon-\varepsilon^2},
\tag{13}
\]

which is exactly the asymptotic Hellinger floor in `MC-363`, and

\[
\boxed{
\lambda_\delta
=\frac12\log\frac1{2\varepsilon-\varepsilon^2},
}
\tag{14}
\]

which is exactly the asymptotic per-direction log-affinity tariff in `MC-364`.

Consequently, for fixed `0<\varepsilon<1` and even `R\to\infty`, the coordinatewise BSC family simultaneously realizes, up to the exponentially small puncture correction, the binary-entropy information scale, the sharp Jensen--Shannon/Hellinger conversion, the normalized Hellinger edge scale, and the negative-log-affinity depth scale derived in `MC-361`--`MC-364`.

This is a decisive boundary for the current generic endpoint branch:

\[
\boxed{
\text{the tariffs themselves cannot rule out an abstract product transcript.}
}
\tag{15}
\]

Any further obstruction must add **source-specific structure** that excludes or quantitatively prices this BSC-like realization. For the Möbius program, the live task is therefore no longer to sharpen an architecture-free information/Hellinger/Bhattacharyya inequality. It is to prove that an actual Möbius-derived transcript cannot supply one independently noisy, sufficiently discriminating observation per source direction at the required precision/depth, or to identify the arithmetic component that really does pay that cost.

No estimate for `M(x)` follows.

## 1. Exact edge geometry of the coordinatewise BSC

For one binary coordinate, the two conditional output laws are

\[
P_+=(1-\delta,\delta),
\qquad
P_-=(\delta,1-\delta).
\]

Their Hellinger affinity is

\[
\begin{aligned}
\operatorname{Aff}(P_+,P_-)
&=\sqrt{(1-\delta)\delta}+\sqrt{\delta(1-\delta)}\\
&=2\sqrt{\delta(1-\delta)},
\end{aligned}
\]

which proves `(1)` for a single coordinate.

If `x,x'` differ only in coordinate `i`, all other component laws coincide. Hellinger affinity tensorizes over the product transcript, so every common factor contributes affinity one and the changed coordinate contributes exactly `(1)`. This proves `(1)`--`(4)` without any inequality.

For the Jensen--Shannon divergence, the equal mixture of `P_+` and `P_-` is uniform. Therefore

\[
\operatorname{JS}(P_+,P_-)
=\log2-h(\delta).
\tag{16}
\]

Also

\[
1-H^2(P_+,P_-)
=2\sqrt{\delta(1-\delta)}.
\]

The inversion formula defining `Phi` in `MC-363` sends this affinity back to the binary posterior parameter `delta`; hence `(16)` is exactly `Phi(H^2)`. This is the binary-symmetric equality case already identified abstractly by the sharp envelope in that finding.

## 2. Puncturing changes only an exponentially small amount of information

The full `R`-cube has `2^(R-1)` undirected edges in each direction. Removing one source vertex deletes exactly one incident edge in each direction, leaving

\[
2^{R-1}-1=\frac{m-1}{2}
\]

surviving edges per direction. Substitution into the normalization

\[
\mathfrak H_1
=\frac2m\sum_{e\in E(\Xi)}H^2(P_x,P_{x'})
\]

gives `(6)` exactly.

The information comparison is equally elementary. Conditional on any source state, the product BSC contributes exactly `Rh(delta)` nats of output entropy, proving `(7)`.

Write the binary channel as addition of an independent noise vector on the group `(F_2)^R`. Since conditioning on the noise vector turns `Y` into a bijective translate of `X`,

\[
H(Y)\ge H(Y\mid Z)=H(X)=\log m.
\]

The opposite bound is simply maximal entropy on `2^R` output states. Equations `(10)` and `(11)` follow. Thus the missing source vertex affects the per-block information by at most

\[
\log\frac{2^R}{2^R-1},
\]

which is exponentially small, not merely `o(R)`.

This also shows why the `O(R/m)` boundary corrections in the general punctured-cube inequalities are harmless for sharpness at fixed error: the BSC construction reaches the same extensive coefficient with a much smaller direct entropy deficit.

## 3. Exact small-error matching of the MC-363 and MC-364 currencies

At matched-filter error parameter `epsilon`, `MC-361` supplies the information floor

\[
L_R=\log m-Rh(\varepsilon/2).
\]

Choosing `delta=epsilon/2` makes `(10)` attain that lower floor within `(11)`.

The sharp envelope of `MC-363` then predicts the asymptotic edge cost

\[
z_\varepsilon
=1-\sqrt{2\varepsilon-\varepsilon^2}.
\]

Equation `(2)` gives exactly this value. There is no loss in the pairwise divergence conversion, and because all surviving edges carry the same value there is no Jensen heterogeneity loss either.

Finally, the multiplicative affinity coordinate of `MC-364` gives

\[
\Lambda_i
=-\log(1-z_\varepsilon)
=-\log\sqrt{2\varepsilon-\varepsilon^2},
\]

which is `(14)`. Hence the logarithmic divergence

\[
\frac12\log\frac1\varepsilon+O(1)
\qquad(\varepsilon\downarrow0)
\]

is not an artifact of a loose proof. It is the exact Bhattacharyya depth of the simplest classical binary-symmetric observation achieving the same edge discrimination.

At `epsilon=0`, the channel becomes noiseless, edge affinity is zero, and `lambda_delta=+infinity`. This is again consistent with `MC-364`: one perfectly source-revealing component per coordinate pays the exact-endpoint tariff through mutual singularity.

## 4. What this rules out and what remains live

The findings `MC-361`--`MC-364` remain valid and useful admission theorems, but the present equality family closes a tempting continuation: **more architecture-free sharpening of the same information/Hellinger/product-affinity currencies cannot by itself create a Möbius obstruction.**

In particular, none of the following can be inferred from the existing tariff alone:

- that a source-independent product transcript is impossible;
- that the required near-endpoint discrimination needs super-logarithmic Bhattacharyya depth;
- that many weak components are intrinsically inconsistent with the endpoint, provided their cumulative depth reaches `(14)`;
- that a finite number of components is impossible when one component per direction is allowed to become sufficiently accurate;
- that the endpoint tariff distinguishes the rational-prime Möbius source from an abstract binary source.

A useful next theorem must therefore place an **upper** bound on the source discrimination actually available to an arithmetic construction. Examples of genuinely new load-bearing input would include a proved precision/noise floor, a restriction on which source coordinates a component can depend on, a bounded source-direction Bhattacharyya budget derived from arithmetic data, or a theorem showing that the natural Möbius observation channel necessarily identifies many source directions only through a shared low-capacity statistic.

Without such a source-side upper theorem, replacing Hellinger by another divergence or further optimizing the lower conversion only changes the currency of a resource that an abstract BSC can already supply at the required scale.

## 5. Prior art and novelty audit

The binary symmetric channel, its symmetric capacity `log 2-h(delta)` in nats, and the Bhattacharyya parameter used to measure reliability of binary-input channels are classical information theory. Arıkan's channel-polarization framework uses symmetric capacity and the Bhattacharyya parameter as standard binary-channel functionals; later Blackwell-measure treatments explicitly place Hellinger affinity and Bhattacharyya reliability in the same binary-input channel language.

The tensorization of Hellinger affinity and additivity of negative log-affinity are likewise classical; `MC-364` already records Bhattacharyya's divergence and Kakutani's product-Hellinger theory as the relevant prior-art boundary. `MC-363` already proves and audits the sharp Jensen--Shannon/Hellinger envelope and identifies the binary-symmetric equality case.

A targeted literature check on 18 September 2026 found no basis for treating the BSC formulas, their product tensorization, or the capacity/Bhattacharyya relation as new. In particular, E. Arıkan, *Channel polarization: A method for constructing capacity-achieving codes for symmetric binary-input memoryless channels*, IEEE Transactions on Information Theory **55** (2009), 3051--3073, DOI `10.1109/TIT.2009.2021379`, treats symmetric capacity and Bhattacharyya reliability as standard primitives for binary-input memoryless channels; N. Goela and M. Raginsky, *Channel Polarization through the Lens of Blackwell Measures*, IEEE Transactions on Information Theory **66** (2020), 622--648, arXiv `1809.05073`, treats Hellinger affinity and Bhattacharyya-type channel functionals in the same setting.

The durable Mathia delta is only the **joint specialization** of these classical equality mechanisms to the punctured reciprocal endpoint: equations `(6)`, `(10)`--`(14)` show that the complete chain of recent generic lower tariffs is simultaneously asymptotically attainable. The result is therefore a negative frontier classification, not a new theorem in information theory.

## 6. Falsification tests and boundaries

This finding makes no claim that the coordinatewise BSC is an actual Möbius-derived observation mechanism. It is deliberately an abstract matched channel used to test whether the generic endpoint inequalities alone can be contradictory.

The exact statements can be falsified directly:

1. for every surviving one-bit source edge, direct calculation must give affinity `(1)` and Hellinger square `(2)`;
2. product tensorization must leave the edge affinity unchanged because all untouched coordinate laws coincide;
3. the punctured cube must have exactly `(m-1)/2` surviving undirected edges per direction, giving `(6)`;
4. direct entropy calculation must give `H(Y|X)=Rh(delta)` and the sandwich `(8)`--`(11)`;
5. at `delta=epsilon/2`, equations `(13)` and `(14)` must match the asymptotic `MC-363` and `MC-364` tariffs exactly.

The result does **not** prove that the dephasing inequality preceding the information floor is itself exactly attained by this channel at every finite `R`; the sharpness claim is from the `MC-361` information floor through the `MC-364` source-independent product tariff, with the puncture correction made explicit. Nor does it transfer any probabilistic channel statement to deterministic Möbius cancellation.

A future arithmetic theorem that bounds the available source-direction affinity away from this BSC equality family, or proves that an actual Möbius transcript cannot factor into such coordinatewise observations, lies outside the negative conclusion and would be the correct next frontier.

## Consequence for the research line

The generic reciprocal-endpoint information branch has reached a natural closure point. `MC-363` made the JS/Hellinger conversion sharp; `MC-364` exposed the correct additive product currency; the present finding supplies an explicit equality family showing that those tariffs are jointly attainable at their stated scale.

The next substantive move should therefore be arithmetic rather than another divergence refinement: identify a concrete Möbius-derived transcript and prove an independent **upper** theorem for its source-direction discrimination budget, or abandon this endpoint architecture if no source-natural restriction is available. Until such an upper theorem exists, the abstract information tariff is an admission condition, not an obstruction to Möbius cancellation.