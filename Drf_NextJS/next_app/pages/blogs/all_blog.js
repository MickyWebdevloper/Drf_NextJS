// pages/posts/[id].js
import { useRouter } from 'next/router'

const all_blog = ({ posts }) => {

    const router = useRouter()


    return (
        <>
            {posts.map((post) => (
                <li key={post.slug}>
                    <h3>{post.title}</h3>
                    <p>{post.content}</p>
                </li>
            ))}
        </>
    )
}

// This function gets called at build time
export async function getStaticPaths() {
    const res = await fetch(`http://127.0.0.1:8000/detail/${slug = slug}`)
    const one_data = await res.json()


    return {
        // Only `/posts/1` and `/posts/2` are generated at build time
        paths: [{ params: { slug: one_data } }],
        // Enable statically generating additional pages
        // For example: `/posts/3`
        fallback: true,
    }
}



export async function getStaticProps(context) {
    const res = await fetch(' http://127.0.0.1:8000/')
    const posts = await res.json()


    return {
        props: { posts }, // will be passed to the page component as props
        revalidate: 10, // In seconds
    }
}

export default all_blog