# VIS-332 — Wang smoothing preserves regularly varying secondary scales except the constant summatory mode

## Claim

Let

`A(x)=sum_(n<=x) Lambda(n)^2`

and let Wang's symmetric squared-von-Mangoldt source profile be

`S(x)=x^(-2) sum_(n<=x) n Lambda(n)^2 + x^2 sum_(n>x) Lambda(n)^2/n^3`.

Assume that for some `c!=0`, some `-1<alpha<3`, and some eventually positive slowly varying function `L`,

`A(x)=x log x-x + c x^alpha L(x)(1+o(1))`.

If `alpha!=0`, then

`S(x)=log x + c m(alpha) x^(alpha-1)L(x)(1+o(1))`,

where

`m(alpha)=4 alpha/[(alpha+1)(3-alpha)]`

`        = alpha * 4/[4-(alpha-1)^2]`.

Thus every nonconstant regularly varying secondary scale in the summatory squared-von-Mangoldt source survives Wang's symmetric smoothing with the same regular-variation exponent. In particular,

`m(1)=1`.

So a coherent PNT-scale secondary asymptotic

`A(x)=x log x-x+c x L(x)(1+o(1))`

passes to

`S(x)=log x+c L(x)(1+o(1))`

with the same leading coefficient. Wang's smoothing cannot by itself suppress such a secondary term below its natural scale.

The exceptional index is `alpha=0`. There the two leading Karamata contributions cancel and one gets only

`S(x)-log x=o(x^(-1)L(x))`.

This zero is not a blind frequency of the smoothing kernel from `VIS-292`: the Green/Mellin multiplier remains nonzero. It comes from the extra factor `alpha` introduced when a summatory secondary term is converted back to source mass.

**Evidence/status:** `EXACT-TRANSFORM + CLASSICAL-KARAMATA + DERIVED-ASYMPTOTIC + NEGATIVE-CONTROL + NO-NOVELTY-CLAIM`.

This result does not assert that the actual squared-von-Mangoldt remainder has a regularly varying asymptotic, fixed sign, or nonzero secondary coefficient. In particular, the Korobov--Vinogradov input in `VIS-291` is an upper envelope, not such an asymptotic. The conclusion is a structural control on what Wang's smoothing can do to a coherent regularly varying secondary component.

## 1. Exact transform of the summatory remainder

Stieltjes integration by parts gives, for `x>=2`,

`S(x) = -x^(-2) integral_1^x A(t) dt`
`       +3x^2 integral_x^infinity A(t)t^(-4) dt`.

Indeed, the boundary term `A(x)/x` from the lower sum cancels exactly with the boundary term `-A(x)/x` from the upper tail.

Put

`M(t)=t log t-t`,

`E(t)=A(t)-M(t)`.

A direct integration of `M` gives

`-x^(-2) integral_1^x M(t)dt`
` +3x^2 integral_x^infinity M(t)t^(-4)dt`
` = log x - 3/(4x^2)`.

Therefore the source-profile remainder has the exact representation

`S(x)-log x`
` = -x^(-2) integral_1^x E(t)dt`
`   +3x^2 integral_x^infinity E(t)t^(-4)dt`
`   -3/(4x^2)`.

This identity exposes the only place where a source-specific improvement over the absolute Korobov--Vinogradov transfer can occur: cancellation between the signed lower and upper transforms of the actual summatory remainder `E`.

## 2. Karamata transfer of a regularly varying secondary term

Under the hypothesis

`E(t)=c t^alpha L(t)(1+o(1))`,

Karamata's integration theorem applies to both terms because `alpha>-1` for the lower integral and `alpha<3` for the weighted tail. It gives

`integral_1^x E(t)dt`
` ~ c x^(alpha+1)L(x)/(alpha+1)`,

and

`integral_x^infinity E(t)t^(-4)dt`
` ~ c x^(alpha-3)L(x)/(3-alpha)`.

Hence

`S(x)-log x`
` ~ c x^(alpha-1)L(x)`
`    [-1/(alpha+1)+3/(3-alpha)]`

whenever the bracket is nonzero. Simplifying,

`-1/(alpha+1)+3/(3-alpha)`
` = 4 alpha/[(alpha+1)(3-alpha)]`.

For `alpha!=0` this proves the stated asymptotic. For `alpha=0`, the two leading terms are equal and opposite, so their difference is `o(x^(-1)L(x))`; the explicit `O(x^-2)` endpoint term is smaller because positive slowly varying functions decay more slowly than every negative power.

## 3. Relation to the Green/Mellin multiplier

`VIS-292` identifies Wang's logarithmic smoothing kernel as

`K(u)=exp(-2|u|)`

with Mellin multiplier

`4/(4-w^2)`.

The coefficient above can be written

`m(alpha)=alpha * 4/[4-(alpha-1)^2]`.

The factor

`4/[4-(alpha-1)^2]`

is exactly Wang's nonvanishing Mellin multiplier evaluated at the power corresponding to the source secondary term. The additional `alpha` is the passage from the summatory law `A(x)` to its source measure.

This explains the exceptional `alpha=0` mode without contradicting `VIS-292`: the smoothing filter itself has not annihilated a Mellin mode. A constant summatory offset contributes no leading differentiated source density, so its first-order image cancels between the two Stieltjes tails.

## 4. Consequences for PNT-shaped subpower envelopes

The Korobov--Vinogradov-shaped factor used in `VIS-291`,

`L_KV(x)=exp(-c (log x)^(3/5)(log log x)^(-1/5))`,

is slowly varying as a function of `x`. Therefore, if the squared-von-Mangoldt summatory remainder had a coherent secondary asymptotic

`E(x) ~ c_1 x L_KV(x)`,

then `alpha=1` and the transfer coefficient is exactly one:

`S(x)-log x ~ c_1 L_KV(x)`.

So the symmetric Wang kernel does not manufacture an exponent improvement by smoothing a coherent PNT-scale secondary term. The same applies to any other `x L(x)` secondary asymptotic with slowly varying `L`.

More generally, a coherent power secondary `E(x)~c x^(1-delta)L(x)` is transferred with the same power `x^(-delta)` and coefficient

`4(1-delta)/[(2-delta)(2+delta)]`,

provided `-1<1-delta<3` and `delta!=1`. This is consistent with `VIS-330`: a true fixed-power source-profile remainder is analytically expensive, and Wang's symmetric smoothing does not generically create such a power by changing the exponent of a coherent source term.

## 5. Prior art and evidence boundary

The regular-variation input is classical. See N. H. Bingham, C. M. Goldie, and J. L. Teugels, **Regular Variation**, Encyclopedia of Mathematics and its Applications 27, Cambridge University Press (1987), DOI `10.1017/CBO9780511721434`, especially the Karamata integration theory in Chapter 1. Karamata's theorem gives the two integral asymptotics used above; no novelty is claimed for that theorem or for regular-variation calculus.

The Mathia-specific specialization is the exact two-tail transform induced by Wang's symmetric squared-von-Mangoldt coefficients and its explicit transfer multiplier `m(alpha)`. The Green/Mellin representation itself is already established in `VIS-292`.

The important limitation is that `VIS-291` supplies only

`E(x)=O(x L_KV(x))`,

not a one-signed regularly varying asymptotic. The actual PNT remainder is oscillatory and can have cancellations not represented by the hypothesis here. Therefore `VIS-332` does **not** prove that Wang's actual source remainder attains the Korobov--Vinogradov envelope, nor that a sharper source-specific bound is impossible. It proves only that such a gain cannot be credited to Wang's smoothing annihilating a coherent regularly varying secondary scale.

## Dependencies

- `VIS-291`: supplies the current unconditional Korobov--Vinogradov upper envelope for the complete fixed-power Wang statistic.
- `VIS-292`: identifies the exact Green/Mellin smoothing kernel and its nonvanishing multiplier.
- `VIS-293`: identifies the zeta-zero pole divisor of the squared-von-Mangoldt source transform.
- `VIS-330`: prices true fixed-power real-axis savings by the zero-free half-plane they force.
- `VIS-331`: separates positive linear logarithmic decay from the remaining subpower Mellin corridor.
- `CLUE-wang-fixed-source-packet-localization`: accepted clue whose remaining source-specific branch is narrowed here.

## Research consequence

The accepted Wang source clue can now be sharpened. A candidate improvement over the generic Korobov--Vinogradov transfer must exploit something absent from a coherent regularly varying secondary model: signed oscillation of the actual summatory remainder, cancellation between its lower and upper Stieltjes tails, a source-specific secondary expansion with non-regular structure, or genuinely stronger arithmetic input.

Merely observing that Wang's kernel is smooth, symmetric, or attenuating is not enough. For the PNT-relevant index `alpha=1`, a coherent slowly varying secondary term passes through with multiplier exactly one. The next useful test is therefore to expose and quantify **signed arithmetic cancellation in the actual `Lambda^2` remainder**, then propagate that gain through Wang's complete error budget. That is a separate research question and is not pursued further in this invocation.