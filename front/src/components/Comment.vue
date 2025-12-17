<script setup>
const props = defineProps({
    author: String,
    date: String,
    text: String
});
</script>

<template>
    <div class="comment">
        <div class="heather">
            <div class="author">
                <img src="@/assets/images/avatar.png" :alt="`Avatar de ${author}`" class="avatar" />
                <span class="comment-author">{{ author }}</span>
                <span class="comment-date">{{ date }}</span>
            </div>
            <div class="report">
                <img src="@/assets/images/reportar.png" alt="Reportar comentario" class="report-icon" />
                <button type="button" class="report-btn">Reportar</button>
            </div>
        </div>

        <div class="text">
            <p class="comment-text">{{ text }}</p>
        </div>
        
    </div>
</template>

<style scoped>
.comment {
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    padding: 16px;
    margin-bottom: 16px;
    background-color: #fafafa;
    display: flex;
    flex-direction: column;
    gap: 12px;
}

.heather {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px
}

.author {
    display: flex;
    align-items: center;
    gap: 10px;
    font-weight: bold;
    margin-bottom: 8px;
    color: var(--color-1, #2c3e50);
}

.avatar {
    width: 32px;
    height: 32px;
    border-radius: 50%;
    object-fit: cover;
}

.comment-author {
    margin-right: 8px;
}

.comment-date {
    font-size: 0.75rem;
    color: #888;
}

.comment-text {
    font-size: 1rem;
    color: #333;
    margin-bottom: 12px;
}

.report {
    display: flex;
    align-items: center;
    gap: 6px;
}

.report-icon {
    width: 18px;
    height: 18px;
}

.report-btn {
    background: none;
    border: none;
    color: #e74c3c;
    cursor: pointer;
    font-size: 0.95rem;
    padding: 2px 6px;
    border-radius: 4px;
    transition: background 0.2s;
}
.report:hover {
    border: #e74c3c 0.7px solid;
    border-radius: 5px;
    padding: 5px;
    background: #ffeaea;
}
</style>